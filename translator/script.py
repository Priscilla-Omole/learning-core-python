from translate import Translator

translator = Translator(to_lang="ja")
try:  
    with open('translator/text.txt', mode= 'r') as my_file:
       file = my_file.read()
       translation = translator.translate(file)
       with open('translator/text_ja.txt', mode= 'w') as my_file_2:
          my_file_2.write(translation)
except FileNotFoundError as err:
   print("Check your file path!")
    