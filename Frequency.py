from manim import *

RED = "#FF644E"
BLUE = "#00a2ff"

class SineWaveScene(Scene):
    def construct(self):
        # Create a sine wave using the ParametricFunction
        sine_wave1 = ParametricFunction(
            lambda t: np.array([t, np.sin(0.5*t), 0]),
            t_range=np.array([-3*PI, 3*PI]),
            color=RED
        ).shift(2.5*DOWN)
        sine_wave2 = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]),
            t_range=np.array([-3*PI, 3*PI]),
            color=WHITE
        )
        sine_wave3 = ParametricFunction(
            lambda t: np.array([t, np.sin(2*t), 0]),
            t_range=np.array([-3*PI, 3*PI]),
            color=BLUE
        ).shift(2.5*UP)

        # Add the sine wave to the scene
        self.add(sine_wave1, sine_wave2, sine_wave3)
