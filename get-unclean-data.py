import orchest
import pandas as pd
from sklearn import datasets

# Explicitly cache the data in the "/data" directory since the
# kernel is running in a Docker container, which are stateless.
# The "/data" directory is a special directory managed by Orchest
# to allow data to be persisted and shared across pipelines and
# even projects.

train = pd.read_csv(r"data/train.csv")

print(train.shape)

test = pd.read_csv(r"data/test.csv")

print(test.shape)

orchest.output((train, test), name="data")
print("Success!")