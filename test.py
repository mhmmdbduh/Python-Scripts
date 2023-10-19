import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\inazu\\Downloads\\paspor\\ffmpeg-2023-09-07-git-9c9f48e7f2-full_build\\bin\\ffmpeg.exe'


# Sample S&P500 data
data = {
    'Date': ['2023-09-21', '2023-09-22', '2023-09-25', '2023-09-26', '2023-09-27'],
    'S&P500': [4330.00, 4320.06, 4337.44, 4273.53, 4274.51]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize an empty line plot
line, = ax.plot([], [], marker='o', linestyle='-', color='b', label='S&P500')

# Set plot title and labels
ax.set_title('S&P500 Stock Price')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Function to update the plot for each frame
def update(frame):
    date = df['Date'][:frame + 1]
    price = df['S&P500'][:frame + 1]
    line.set_data(date, price)
    return line,

# Create an animation object
ani = animation.FuncAnimation(fig, update, frames=len(df), blit=True)

# Save the animation as a video using FFmpeg
Writer = animation.FFMpegWriter(fps=2, metadata=dict(artist='Me'), bitrate=1800)
ani.save('stock_price_animation.mp4', writer=Writer)

# Show the plot (optional)
plt.grid()
plt.tight_layout()
plt.show()
