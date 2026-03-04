class ModelReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.state = {}

    def act(self, room, current_temp):
        previous = self.state.get(room)

        if current_temp < self.desired_temp:
            action = "Heater ON"
        else:
            action = "Heater OFF"

        if previous == action:
            result = "No change"
        else:
            result = action
            self.state[room] = action

        return result


rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22

agent = ModelReflexAgent(desired_temperature)

for room, temp in rooms.items():
    action = agent.act(room, temp)
    print(room, "Temp =", temp, "->", action)