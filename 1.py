import pandas as pd
import numpy as np
df = pd.read_csv('2021-12-13T1341_Grades-S2108-STAT-3090-019-89839.csv')

# if all of your LAs (learning activities) start with 'LA', the canvas will rename your LAs ending with ')'.
LAName = [col for col in df if col.startswith('LA') and col.endswith(')')]
LAScore= df[LAName].fillna(0).mean(axis=1)
df['LAScoreDrop5'] = pd.DataFrame(np.mean(np.sort(df[LAName].fillna(0), axis=1)[:, 5:], axis=1)).round(1)

#JMP project scores
ProjectName = [col for col in df if col.startswith('Project') and col.endswith(')')]
df['ProjectScore'] = df[ProjectName].fillna(0).mean(axis=1).round(1)

# Hawkes Learner's options
HLOName = [col for col in df if col.startswith('Learner') and col.endswith(')')]
HLOScore= df[HLOName].fillna(0).mean(axis=1)
df['HLOScoreDrop4'] = pd.DataFrame(np.mean(np.sort(df[HLOName].fillna(0), axis=1)[:, 4:], axis=1)).round(1)

# Hawkes webtest scores
HWebtestName = [col for col in df if col.startswith('Web Test') and col.endswith(')')]
HWebtestScore= df[HWebtestName].fillna(0).mean(axis=1)
df['HWebtestScoreDrop2'] = pd.DataFrame(np.mean(np.sort(df[HWebtestName].fillna(0), axis=1)[:, 2:], axis=1)).round(1)

# Unit test
UnitTestName = [col for col in df if col.startswith('Unit Test') and col.endswith(')')]
df['UnitTestScore'] = df[UnitTestName].fillna(0).mean(axis=1)
df['UnitTestScoreDrop1'] = pd.DataFrame(np.mean(np.sort(df[UnitTestName].fillna(0), axis=1)[:, 1:], axis=1)).round(1)

# Final Exam
FinalExamName = [col for col in df if col.startswith('Final Exam') and col.endswith(')')]
df['FinalExamScore'] = df[FinalExamName].fillna(0).mean(axis=1)


#Weighted Average

df['FinalScoreMethod1'] = 0.05 * df['LAScoreDrop5']  + 0.1 * df['ProjectScore'] + 0.05 * df['HLOScoreDrop4'] + 0.05 * df['HWebtestScoreDrop2'] + 0.45 * df['UnitTestScore'] + 0.3 * df['FinalExamScore'] 

df['FinalScoreMethod2'] = 0.05 * df['LAScoreDrop5']  + 0.1 * df['ProjectScore'] + 0.05 * df['HLOScoreDrop4'] + 0.05 * df['HWebtestScoreDrop2'] + 0.3 * df['UnitTestScoreDrop1'] + 0.45 * df['FinalExamScore'] 

df['FinalScore'] = (df[['FinalScoreMethod1', 'FinalScoreMethod2']].max(axis=1)).round(1)
df['Version'] = 'A'
#print(df[['SIS User ID','Version','FinalScore']].fillna(0).to_csv(index=False))
df['absents'] = np.random.randint(0,6,size=26)
print(df[['SIS User ID','absents','FinalScore']].fillna(0).to_csv(index=False))
