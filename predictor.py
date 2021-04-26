### Custom definitions and classes if any ###
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def predictRuns(testInput):
    prediction = 0
    ### Your Code Here ###
    raw_data = pd.read_csv('all_matches.csv')
    raw_data.columns
    df = raw_data
    df = df.drop(['match_id','start_date','batting_team','bowling_team','striker','non_striker','bowler','extras', 'wides', 'noballs', 'byes', 'legbyes',
        'penalty', 'wicket_type', 'player_dismissed', 'other_wicket_type',
        'other_player_dismissed'],axis = 1)
    df = df.loc[(df['ball'] >= 0.1) & (df['ball'] <= 5.6)]
    df = df.loc[(df['venue'] == 'MA Chidambaram Stadium, Chepauk, Chennai') | (df['venue'] == 'MA Chidambaram Stadium, Chepauk') ]
    df = df.drop(['venue'],axis = 1)
    df = pd.get_dummies(df)
    df.fillna(0,inplace=True)
    train = df[0:3000]
    test = df[3001:]
    X_train = train.drop('runs_off_bat',axis = 1)
    y_train = train['runs_off_bat']
    X_test = test.drop('runs_off_bat',axis = 1)
    true_p = test['runs_off_bat']
    from sklearn.linear_model import LogisticRegression
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train)
    pred = logreg.predict(X_test)
    score = logreg.score(X_test,true_p)*100
    prediction = int(score)  
   
    return prediction
