
import math

# Constants
DECIBEL_THRESHOLD_LAWN_MOWER = 90  # Decibel threshold of a lawnmower

# Material Properties (Source: Research)
MATERIAL_INSULATION = {
    "glass": 0.05,  # Insulation value for glass
    "wood": 0.2,    # Insulation value for wood
    "brick": 0.8    # Insulation value for brick
}

MATERIAL_ABSORPTION = {
    "glass": 0.2,   # Sound absorption coefficient for glass
    "wood": 0.4,    # Sound absorption coefficient for wood
    "brick": 0.7    # Sound absorption coefficient for brick
}

# Function to calculate sound intensity
def calculate_sound_intensity(decibels):
    return 10 ** ((decibels - 120) / 10)

# Function to calculate sound pressure level
def calculate_sound_pressure_level(intensity):
    return 20 * math.log10(intensity / (10 ** -12))

# Function to calculate sound transmission loss
def calculate_transmission_loss(material, distance):
    insulation = MATERIAL_INSULATION[material]
    loss = 20 * math.log10(distance) + insulation
    return loss

# Function to calculate the effective sound pressure level
def calculate_effective_sound_pressure_level(sound_pressure_level, transmission_loss):
    return sound_pressure_level - transmission_loss

# Function to check if the sound is within the threshold
def is_sound_within_threshold(sound_pressure_level, threshold):
    return sound_pressure_level > threshold

def main():
    # Research the decibel threshold of a lawnmower
    lawnmower_decibel_threshold = DECIBEL_THRESHOLD_LAWN_MOWER

    # Research the materials that better insulate sound
    glass_insulation = MATERIAL_INSULATION["glass"]
    wood_insulation = MATERIAL_INSULATION["wood"]
    brick_insulation = MATERIAL_INSULATION["brick"]

    # Research how well each material absorbs sound
    glass_absorption = MATERIAL_ABSORPTION["glass"]
    wood_absorption = MATERIAL_ABSORPTION["wood"]
    brick_absorption = MATERIAL_ABSORPTION["brick"]

    # Get user input for the distance of the lawnmower from the building
    distance = float(input("Enter the distance of the lawnmower from the building (in meters): "))

    # Calculate the sound intensity and pressure level of the lawnmower
    sound_intensity_lawnmower = calculate_sound_intensity(lawnmower_decibel_threshold)
    sound_pressure_level_lawnmower = calculate_sound_pressure_level(sound_intensity_lawnmower)

    # Calculate the transmission loss for each material
    glass_transmission_loss = calculate_transmission_loss("glass", distance)
    wood_transmission_loss = calculate_transmission_loss("wood", distance)
    brick_transmission_loss = calculate_transmission_loss("brick", distance)

    # Calculate the effective sound pressure level for each material
    glass_effective_sound_pressure_level = calculate_effective_sound_pressure_level(sound_pressure_level_lawnmower, glass_transmission_loss)
    wood_effective_sound_pressure_level = calculate_effective_sound_pressure_level(sound_pressure_level_lawnmower, wood_transmission_loss)
    brick_effective_sound_pressure_level = calculate_effective_sound_pressure_level(sound_pressure_level_lawnmower, brick_transmission_loss)

    # Check if the sound is within the threshold for each material
    glass_sound_within_threshold = is_sound_within_threshold(glass_effective_sound_pressure_level, DECIBEL_THRESHOLD_LAWN_MOWER)
    wood_sound_within_threshold = is_sound_within_threshold(wood_effective_sound_pressure_level, DECIBEL_THRESHOLD_LAWN_MOWER)
    brick_sound_within_threshold = is_sound_within_threshold(brick_effective_sound_pressure_level, DECIBEL_THRESHOLD_LAWN_MOWER)

    # Print the results
    print("Results:")
    print("--------")
    print("Glass:")
    print(f" Insulation: {glass_insulation}")
    print(f" Absorption: {glass_absorption}")
    print(f" Transmission Loss: {glass_transmission_loss:.2f} dB")
    print(f" Effective Sound Pressure Level: {glass_effective_sound_pressure_level:.2f} dB")
    print(f" Sound within Threshold: {'Yes' if glass_sound_within_threshold else 'No'}")
    print()
    print("Wood:")
    print(f" Insulation: {wood_insulation}")
    print(f" Absorption: {wood_absorption}")
    print(f" Transmission Loss: {wood_transmission_loss:.2f} dB")
    print(f" Effective Sound Pressure Level: {wood_effective_sound_pressure_level:.2f} dB")
    print(f" Sound within Threshold: {'Yes' if wood_sound_within_threshold else 'No'}")
    print()
    print("Brick:")
    print(f" Insulation: {brick_insulation}")
    print(f" Absorption: {brick_absorption}")
    print(f" Transmission Loss: {brick_transmission_loss:.2f} dB")
    print(f" Effective Sound Pressure Level: {brick_effective_sound_pressure_level:.2f} dB")
    print(f" Sound within Threshold: {'Yes' if brick_sound_within_threshold else 'No'}")

if __name__ == "__main__":
    main()
