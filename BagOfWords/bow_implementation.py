import pandas as pd


df = pd.read_table(r'C:\Users\NITHIN\Desktop\Spam_Classification\smsspamcollection\SMSSpamCollection', sep ='\t', header=None,names = ['label', 'sms_message'])


df['label'] = df.label.map({'ham':0,'spam':1})
print(df.shape)
lower_case= []
messages = df['sms_message']
for i in range(0, 5571):
    lower_case.append(messages[i].lower())

print(lower_case)
