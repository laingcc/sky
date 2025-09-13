# Hand-Controlled Particle Universe

This project uses your webcam to create a real-time interactive particle universe. Your hands become emitters of stars and galaxies, allowing you to paint the cosmos with your movements.

## Features

- **Hand Tracking:** Uses MediaPipe to track your hands in real-time.
- **Particle Effects:** Generates stars and galaxies that flow from your hands.
- **Dynamic Background:** Features a subtle, moving starfield.
- **Shooting Stars and UFOs:** Randomly occurring shooting stars and UFOs add to the cosmic ambiance.
- **Fullscreen Mode:** Creates an immersive experience by running in fullscreen.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install the dependencies:**
   Make sure you have Python 3 installed. Then, run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script to start the application:

```bash
python main.py
```

Move your hands in front of the webcam to see the particle effects. Press 'q' to quit the application.

## How it Works

The application captures video from your webcam and uses the MediaPipe library to detect the position of your hands. For each detected hand, it generates a stream of particles, creating a visual effect of stars and galaxies flowing from your fingertips. The background is a procedurally generated starfield with occasional shooting stars and UFOs to enhance the experience.

## License

This project is licensed under the terms of the GPL v3 license. See the [LICENSE](LICENSE) file for more details.
