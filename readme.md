# uncommon hacks


#### Installation
- Clone this repository ```git clone git@github.com:meggrasse/uncommonhacks.git```

#### Usage 
- Text a message to (630) 755-6548 and expect a phone call with the generated music equivalent

#### What we did
- Twilio integration and server
- Sentiment analysis
- Logic of chord generation
- Generating sheet music and .wav file: We used the chord generation logic to write sheet music in the .abc file structure. We used a dictionary of lists to represent the individual component notes of a chord and wrote the .abc file using standard python text file writing methodology. Then we used files from Mdoege's PySynth to produce .wav files from the sheet music represented in the .abc file.   