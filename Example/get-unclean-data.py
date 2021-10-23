import orchest
import pandas as pd
from sklearn.model_selection import train_test_split

# Explicitly cache the data in the "/data" directory since the
# kernel is running in a Docker container, which are stateless.
# The "/data" directory is a special directory managed by Orchest
# to allow data to be persisted and shared across pipelines and
# even projects.

train = pd.read_csv(r"data/creditcard.csv")

print(train.shape)

train, test = train_test_split(train)

# test = pd.read_csv(r"data/test.csv")

# print(test.shape)

orchest.output((train,test), name="data")
print("Success!")