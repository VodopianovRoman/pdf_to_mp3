import pdfplumber
from art import tprint
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', lang='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

            text = ''.join(pages)
            text = text.replace('\n', ' ')

            my_audio = gTTS(text=text, lang=lang)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved successfully!\n---Good luck!---'

    elif Path(file_path).suffix != '.pdf':
        return "Wrong file's format!"
    else:
        return 'File not find.'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example: 'en', 'uk' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, lang=language))

if __name__ == '__main__':
    main()
