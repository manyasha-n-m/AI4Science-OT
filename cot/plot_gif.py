import matplotlib.pylab as pl
from IPython.display import display
from io import BytesIO
from PIL import Image
from typing import List, Union


class PlotGIF:
    '''
    Object used to create GIF files out of graphs. Implements slicing and generator protocols.

    Attributes:
        frames: List[PIL.Image] - List of frames in GIF.
    
    Methods:
        get_frames() -> List[PIL.Image] - Returns PlotGIF.frames
        length() -> int - Returns number of frames in GIF.
        clear() -> None - Removes all frames from GIF.
        pop() -> PIL.Image - Removes the last frame and returns it.
        stamp(fig: int = 1, clear: bool = True) -> None - Saves the given figure as a frame.
        If clear = True, the figure is cleared with pylab.clf() after saving.
        save(path: str, duration: int) -> None - Saves a GIF file to disk at the given path.
        Duration specifies how long the GIF lasts (in seconds).
        show(index: int) -> None - Displays a preview of the frame at the given index.
    '''

    def __init__(self) -> None:
        '''Initializes PlotGIF object.'''

        self.frames = []
        self.__frame = 0

    def __len__(self) -> None:
        '''Returns number of frames in GIF.'''

        return self.length()

    def __str__(self) -> None:
        '''Returns a string representation of GIF.'''

        return f"PlotGIF(num_frames={self.length()})"

    def __getitem__(self, sliced: Union[int, slice]) -> List[Image]:
        '''Returns a slice of frames. Accepts integer indexes and slice objects.'''

        return self.frames[sliced]

    # type hint does not use typing.Self for compatability with Pythons < 3.11

    def __iter__(self) -> "self":
        '''Returns a generator that iterates through each frame in GIF.'''

        self.__frame = 0
        return self

    def __next__(self) -> Image:
        '''Returns the next frame from the generator.'''

        if self.__frame < len(self.frames) - 1:
            self.__frame += 1
            return self.frames[self.__frame]
        else:
            raise StopIteration

    def get_frames(self) -> List[Image]:
        '''Returns list of frames in GIF.'''

        return self.frames

    def length(self) -> int:
        '''Returns number of frames in GIF.'''

        return len(self.frames)

    def clear(self) -> None:
        '''Removes all frames from GIF.'''

        self.frames.clear()

    def pop(self) -> Image:
        '''Removes the last frame and returns it.'''

        return self.frames.pop()

    def stamp(self, fig: int = 1, clear: bool = True) -> None:
        '''
        Adds a frame to GIF.

        Parameters:
            fig: int = 1 - Which graph to save from.
            clear: bool = True - Whether to clear the graph after saving frame.

        Returns:
            None
        '''

        buffer = BytesIO()
        pl.figure(fig).savefig(buffer, format="png")
        self.frames.append(Image.open(buffer))
        if clear:
            pl.clf()

    def save(self, path: str, duration: str) -> None:
        '''
        Saves GIF to disk.
        
        Parameters:
            path: str - Where to save the GIF file.
            duration: str - How long GIF lasts (in seconds).

        Returns:
            None
        '''

        self.frames[0].save(path, format="GIF", append_images=self.frames, save_all=True, duration=duration, loop=0)

    def show(self, index: int) -> None:
        '''Displays a preview of the frame at the given index.'''

        display(self[index])
