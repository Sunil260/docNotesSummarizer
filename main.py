#main for text comprhension
import cohere
from DoctorNote import DoctorNote
import re
import os


def txtToNote(inputFileTxt:str,patientName="John",Token=""):



  noteArr = re.split('r"<.*?>',inputFileTxt)

  a = DoctorNote(patientName,10,noteArr, "token")
  
  return a

def test():

  directory = './data'
  NotesArray = []
  
  for filename in os.listdir(directory):
      f = os.path.join(directory, filename)
      
      text_file = open(f, "r")
      
      try:
       data = text_file.read()
      except:
        pass
      text_file.close()
      
      NotesArray.append(txtToNote(data,"josh","abdkjahuiw98ehn9qwhudnid"))

  id = 1000

  apiKey = '1jAAEzBf6dAOn8PMlWtdzZibcJdxbytVEzKKTNMW'
  co = cohere.Client(apiKey)

  for note in NotesArray:
    try:
      with open('./output/'+ str(id) + '.txt', 'w') as f: 

          for txt in note.__getNote__():
            
            response = co.generate(
              model='xlarge',
              prompt=txt,
              max_tokens=50,
              temperature=0.8,
              k=0,
              p=1,
              frequency_penalty=0,
              presence_penalty=0,
              stop_sequences=["--"],
              return_likelihoods='NONE')
            f.write('Summarization: {}'.format(response.generations[0].text) + "\n")
            





    except FileNotFoundError:
          print("The 'docs' directory does not exist")
    id += 1
  

    
test()


