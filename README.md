# Cambridge Cancer Genomics Challenge

This project uses **Python Version 3.6.**

## Running the pipeline

- Activate the virtual environment `venv` using `source venv/bin/activate`.
- Install the dependencies listed in `requirements.txt`.
- Navigate to the directory containing `main.py`
- Execute the program using `python main.py`. Optionally, use 
`--processes  [num of processes]` to specify how many processes to use
for image processing.
- The program creates the following directories to store the images: 
`transformedImages` and `noisyImages`.

## Running tests

Tests can be run from the command line using `python -m unittests`. 
(Haven't tried it out, used an IDE for development)

## Code Organisation

- ccg-challenge
    - data_pipeline (contains raw data)
    - tests
        - testImgs (images used for testing)
        - test_data_extraction
        - test_file_write
        - test_noise_addition
        - test_transformations
    - utils (modules for the pipeline)
        - DiskWrite 
        - LoadRawImageData
        - Noisy
        - TransformImages
    - venv
    - main.py (Project entry point)
    
## Improvements to be made:

1. Currently, the transformed and the noisy files aren't linked
since processes do not preserve order when being mapped to the image data.
This could be handled through the use of semaphores but needs to be explored further.

2. More detailed logging: Logging is currently done only at checkpoints when one bit of the pipeline 
finishes. This has to be done in greater detail for the sub functions too.

3. More command line arguments to change verbosity level, allow the user to specify data location. 

4. Containerize. I haven't used Docker before and trying to set it up for this might have meant more time
away from core functionality

5. Sort out my IDE so that I can list packages used exclusively by this project rather than all installed on my machine.

6. Improve tests. Currently, some of the tests are pretty barebones version. This is on the assumption that the functions
that they are testing wrap around existing and well tested functions from libraries like numpy and opencv. One way to improve
the tests could be to compare pixel values' frequencies between noiseless and noisy images. Similarly, transformations could
be tested using the appearance of dark spots being below a certain threshold established by the range used. 