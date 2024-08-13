import plotly.graph_objects as go
from random_walk import RandomWalk

# Keep making random walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Convert range to a list
    point_numbers = list(range(rw.num_points))

    # Create the scatter plot using Plotly.
    fig = go.Figure()

    # Add the scatter trace for the random walk points.
    fig.add_trace(go.Scatter(
        x=rw.x_values,
        y=rw.y_values,
        mode='markers',
        marker=dict(
            size=1,
            color=point_numbers,  # Convert range to list
            colorscale='Blues',
            showscale=False
        ),
        showlegend=False  # Hide this trace from the legend
    ))

    # Emphasize the first and last points.
    fig.add_trace(go.Scatter(
        x=[0],
        y=[0],
        mode='markers',
        marker=dict(
            size=10,
            color='green'
        ),
        name='Start'
    ))

    fig.add_trace(go.Scatter(
        x=[rw.x_values[-1]],
        y=[rw.y_values[-1]],
        mode='markers',
        marker=dict(
            size=10,
            color='red'
        ),
        name='End'
    ))

    # Update layout to hide axes and set size.
    fig.update_layout(
        title='Random Walk',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        autosize=True,
        width=1000,  # Adjust the width as needed
        height=700,  # Adjust the height as needed
    )

    # Show the plot.
    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
