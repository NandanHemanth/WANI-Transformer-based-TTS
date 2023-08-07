import matplotlib.pyplot as plt

# Sample data for English, Hindi, and Chinese
english_characters = [14, 35, 36, 39, 32, 35, 38, 40, 97, 108, 84, 103, 96, 150, 121, 109, 114, 115, 104, 327, 425]
english_time = [5.3, 10.4, 8.5, 9.1, 9.1, 7.9, 9.3, 8.1, 15.9, 17.2, 14.9, 13.4, 20.6, 18.4, 14.5, 33.5, 19, 16.9, 18.4, 33.2, 33.8]

hindi_characters = [16, 57, 26, 38, 34, 50, 36, 38, 126, 147, 91, 154, 107, 213, 157, 148, 129, 154, 150, 191, 396]
hindi_time = [7.3, 16.8, 12, 9.7, 10.1, 18.6, 20.1, 11.2, 15.3, 17.7, 14.9, 15.2, 16.7, 21.3, 16.5, 14.9, 12.6, 16.4, 16.7, 32.4, 33.7]

chinese_characters = [4, 20, 16, 24, 18, 30, 17, 17, 50, 61, 49, 73, 61, 43, 57, 49, 56, 64, 61, 191, 396]
chinese_time = [4.9, 9.5, 9.2, 10.4, 9.9, 10.6, 8.8, 8.4, 12.4, 15.8, 14.5, 18.6, 18.4, 16.5, 23.7, 14.7, 19.4, 21.1, 24.7, 33.7, 33.7]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(english_characters, english_time, label='English', marker='o')
plt.plot(hindi_characters, hindi_time, label='Hindi', marker='s')
plt.plot(chinese_characters, chinese_time, label='Chinese', marker='^')

# Adding labels and title
plt.xlabel('Characters')
plt.ylabel('Time (seconds)')
plt.title('Time Taken to Read Characters in Different Languages')

# Adding legend
plt.legend()

# Display the plot
plt.grid(True)  # Add gridlines to the plot
plt.show()
