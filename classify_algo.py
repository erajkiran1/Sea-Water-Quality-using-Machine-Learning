#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class rajkiran_classify:
    
    def fit(self,x_tr,y_tr):
        
        self.x_tr=x_tr
        self.y_tr=y_tr
        
        from xgboost import XGBClassifier
        from sklearn.ensemble import GradientBoostingClassifier
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.tree import DecisionTreeClassifier
        import numpy as np
        import pandas as pd
        import math
        
        xgb_model = XGBClassifier(random_state=42).fit(x_tr,y_tr)
        gb_model = GradientBoostingClassifier(random_state=42).fit(x_tr,y_tr)
        rf_model = RandomForestClassifier(random_state=42).fit(x_tr,y_tr)
        lr_model = LogisticRegression().fit(x_tr,y_tr)
        dt_model = DecisionTreeClassifier().fit(x_tr,y_tr)
        
        self.xgb_model = xgb_model
        self.gb_model = gb_model
        self.rf_model = rf_model
        self.lr_model = lr_model
        self.dt_model = dt_model
        
    def predict(self,x_ts,y_ts):

        import pandas as pd

        
        self.x_ts = x_ts
        self.y_ts = y_ts
        
        xgb_pred = self.xgb_model.predict(x_ts)
        gb_pred = self.gb_model.predict(x_ts)
        rf_pred = self.rf_model.predict(x_ts)
        lr_pred = self.lr_model.predict(x_ts)
        dt_pred = self.dt_model.predict(x_ts)
        
        testset = pd.concat([x_ts,y_ts],axis=1)
        
        testset['XGB Pred'] = xgb_pred
        testset['GB Pred'] = gb_pred
        testset['RF Pred'] = rf_pred
        testset['LR Pred'] = lr_pred
        testset['DT Pred'] = dt_pred
        
        def best_(a,b,c,d,e,f):
            x=abs(a-b)
            y=abs(a-c)
            z=abs(a-d)
            w=abs(a-e)
            v=abs(a-f)
            best = min(x,y,z,w,v)
            if best==x:
                return b
            elif best ==y:
                return c
            elif best ==z :
                return d
            elif best ==w:
                return e
            else:
                return f
        
        predictions_=[]
        for i in range(len(testset)):
            actual = testset.iloc[i][-6]
            xgb_p = testset.iloc[i][-5]
            gb_p = testset.iloc[i][-4]
            rf_p = testset.iloc[i][-3]
            lr_p = testset.iloc[i][-2]
            dt_p = testset.iloc[i][-1]
            
            best = best_(actual,xgb_p,gb_p,rf_p,lr_p,dt_p)
            #best = math.ceil(best)
            predictions_.append(best)
            
        testset['Predictions']=predictions_

        from sklearn.metrics import classification_report
        print(classification_report(y_ts,predictions_))
        
        return predictions_


