import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="RL Agent Demo", layout="centered")
st.title("🤖 Reinforcement Learning Agent Simulation")
st.markdown("This demo visualizes how an RL agent learns to reach the goal in a simple grid world.")

# Parameters
GRID_SIZE = 5
goal_pos = (4, 4)
obstacles = [(1, 1), (2, 3), (3, 1)]
agent_pos = [0, 0]

# Display grid
def draw_grid(agent):
    grid = np.full((GRID_SIZE, GRID_SIZE), "⬜")
    grid[goal_pos] = "🏁"
    for obs in obstacles:
        grid[obs] = "⬛"
    grid[tuple(agent)] = "🤖"
    for row in grid:
        st.write(" ".join(row))

# Simulated policy (dummy movement towards goal)
def next_step(agent):
    x, y = agent
    if x < goal_pos[0]:
        x += 1
    elif y < goal_pos[1]:
        y += 1
    return [x, y]

if st.button("▶️ Run Agent Simulation"):
    agent_pos = [0, 0]
    steps = 0
    while agent_pos != list(goal_pos) and steps < 20:
        draw_grid(agent_pos)
        agent_pos = next_step(agent_pos)
        steps += 1
        time.sleep(0.4)
        st.write("---")
    draw_grid(agent_pos)
    st.success("Agent reached the goal!" if agent_pos == list(goal_pos) else "Stopped.")
