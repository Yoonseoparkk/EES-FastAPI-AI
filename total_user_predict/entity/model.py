import torch.nn as nn


class WithdrawPredictModel(nn.Module):
    def __init__(self, in_features=5, out_features=5, hidden_size=32):
        super(WithdrawPredictModel, self).__init__()

        self.lstm = nn.LSTM(in_features, hidden_size, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, 32)
        self.fc2 = nn.Linear(32, out_features)

    def forward(self, x):
        output, (hidden, cell) = self.lstm(x)
        x = self.fc(output)
        x = self.fc2(x)

        return x
