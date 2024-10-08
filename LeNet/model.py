import torch
import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))  # input(3, 32, 32) output(16, 28, 28) (w-f-2p)/s +1
        x = self.pool1(x)  # output(16, 14, 14)
        x = F.relu(self.conv2(x))  # output(32, 10, 10)
        x = self.pool2(x)  # output(32, 5, 5)
        # 数据通过view函数将图片格式转换为一维向量
        # x = x.view(-1, 32 * 5 * 5)  # output(32*5*5)
        # 使用 torch.flatten 函数来替代 view 方法进行展平操作。flatten 方法提供了一种更直观的方式来展平张量。
        x = torch.flatten(x, start_dim=1)  # 从第二个维度开始展平，第一个维度是batch，保持batch不变
        x = F.relu(self.fc1(x))  # output(120)
        x = F.relu(self.fc2(x))  # output(82)
        x = self.fc3(x)  # output(10)
        return x


# debug 查看模型信息
# input1 = torch.randn([32, 3, 32, 32])
# model = LeNet()
# print(model)
# output = model(input1)
