# OpenCV-Presentations

Use visual gestures to give presentations with OpenCV.

## Usage

- Firstly install all the required packages

```shell
pip install -r requirements.txt
```

- Now, to run the application, simply run the `main.py`

```shell
python3 main.py
```

- Now you can use any of the [supported file types]() and [gestures](#gestures) to give your presentation.

## Gestures

- Move to next slide:
  > _(Above the threshold line)_ Point to right by putting up only your little finger or thumb based on the hand you are using.
- Move to previous slide:
  > _(Above the threshold line)_ Point to left by putting up only your little finger or thumb based on the hand you are using.
- Show a pointer:
  > _(Configured for left hand only)_ Point out your index finger only and a pointer will be shown on the slide image based upon your finger's location.
- Make annotations/drawings:

  > _(Configured for left hand only)_ Point out your index and middle finger together and an annotation will be started and made wherever you move your fingers.
  > The annotations will be removed when you change slides.

- Erase annotations:
  > _(Above the threshold line)_ Point out your index, middle and ring fingers together to erase all the annotations.

## Supported File Types

Currently the following file types are supported:

- jpeg
- png
- svg _(not tested)_
- webp _(not tested)_
