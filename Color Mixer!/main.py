# Color Mixing Game - I have included code for upto three color combinations.
# Add more if you want.

color_01 = input("Enter the first color(blue, red, yellow): ").lower()  # Ask user for input
color_02 = input("Enter the second color(blue, red, yellow): ").lower() # Ask user for input

colors = [color_01, color_02]

print("-" * 50)

print(f"🥼 Let's mix {color_01} + {color_02}\n")

# Mix new colors

if color_01 == color_02: # In case the user enters the same color in both inputs.

    emoji = None

    if color_01 == "red":
        emoji = "❤️"
    elif color_01 == "blue":
        emoji = "🟦"
    elif color_01 == "yellow":
        emoji = "🟡"

    print("🎨 You are mixing the same color!")
    print(f"🧪{color_01} + 🧪{color_02} = {color_01} {emoji}.")

elif "red" in colors and "blue" in colors:
    print(f"🧪{color_01} + 🧪{color_02} = Purple 🟪.")

elif "red" in colors and "yellow" in colors:
    print(f"🧪{color_01} + 🧪{color_02} = Orange 🔶.")

elif "yellow" in colors and "blue" in colors:
    print(f"🧪{color_01} + 🧪{color_02} = Green 🟢.")

else:
    print("❌ Invalid Combo!\nPlease use red, blue, or yellow.")