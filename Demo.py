# def min_edit_distance(word1, word2):
#     m = len(word1)
#     n = len(word2)

#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     for i in range(m + 1):
#         dp[i][0] = i

#     for j in range(n + 1):
#         dp[0][j] = j

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):

#             if word1[i - 1] == word2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(
#                     dp[i - 1][j],      # Deletion
#                     dp[i][j - 1],      # Insertion
#                     dp[i - 1][j - 1]   # Replacement
#                 )

#     return dp[m][n]


# print(min_edit_distance("cat", "cut"))
# print(min_edit_distance("book", "books"))

# a = [1, 2, 3, [4, 5]]

# b = a[:]

# b[-1][0] = 400

# print(a)
# print(b)

# b[2]= 3000

# print(a)
# print(b)
# import numpy as np
# matrix = np.array([[1, 2, 3], 
#                    [4, 5, 6]])

# print(matrix.T)




# import sys

# a = [10, 20, 30]
# b = (10, 20, 30)

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))



# import torch
# import torch.nn as nn
# import torch.optim as optim
# import torchvision
# import torchvision.transforms as transforms

# # Step 1 & 2: Dataset Prepare karna aur DataLoader banana
# transform = transforms.Compose([transforms.ToTensor()])

# train_dataset = torchvision.datasets.MNIST(
#     root='./data', 
#     train=True, 
#     download=True, 
#     transform=transform
# )

# train_loader = torch.utils.data.DataLoader(
#     dataset=train_dataset, 
#     batch_size=64, 
#     shuffle=True
# )

# # Step 3: Neural Network Model Architecture Design karna
# class SimpleNN(nn.Module):
#     def __init__(self):
#         super(SimpleNN, self).__init__()
#         self.fc1 = nn.Linear(28 * 28, 128)  # Input layer (784 pixels -> 128 neurons)
#         self.relu = nn.ReLU()               # Activation function
#         self.fc2 = nn.Linear(128, 10)       # Output layer (128 -> 10 classes for digits 0-9)
        
#     def forward(self, x):
#         x = x.view(-1, 28 * 28)             # Flatten 28x28 image into 1D vector
#         x = self.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# model = SimpleNN()

# # Step 4: Loss Function define karna
# criterion = nn.CrossEntropyLoss()

# # Step 5: Optimizer select karna
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Step 6: Training the Model (Training Loop)
# epochs = 2  # Aap apni zaroorat ke hisaab se epochs badha sakte hain
# print("Training shuru ho rahi hai...")

# for epoch in range(epochs):
#     for images, labels in train_loader:
#         # Forward pass: predictions nikalna[cite: 1]
#         outputs = model(images)
        
#         # Loss calculate karna[cite: 1]
#         loss = criterion(outputs, labels)
        
#         # Backpropagation aur weight update[cite: 1]
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
        
#     print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# # Step 7: Model Evaluation (Testing accuracy)
# correct = 0
# total = 0
# with torch.no_grad():  # Gradient tracking disable karna testing ke liye[cite: 1]
#     for images, labels in train_loader:
#         outputs = model(images)
#         _, predicted = torch.max(outputs.data, 1)
#         total += labels.size(0)
#         correct += (predicted == labels).sum().item()

# print(f"Training Accuracy: {100 * correct / total:.2f}%")

# # Step 8: Model Save karna
# torch.save(model.state_dict(), "model.pth")
# print("Model successfully save ho gaya hai 'model.pth' file me!")


def divide(first, second):
    print("The result is:", first / second)

def swipe_decorator(func):
    def swipe(first, second):
        if first < second:
            first, second = second, first

        return func(first, second)

    return swipe

divide = swipe_decorator(divide)

divide(4, 16)