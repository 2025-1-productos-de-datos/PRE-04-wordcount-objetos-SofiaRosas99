"""Entry point for the homework package."""

# python3 -m homework 10 data/raw data/input data/output

from homework.src.main import main
import argparse

class ArgumentParser:
    def __init__(self):
        
        self.input = None
        self.output = None
    
    def run(self):
        
        



def parse_args():

    

    return parsed_args.input, parsed_args.output


def read_all_lines(input_folder):
    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines






def main():
    argument_parser = ArgumentParser().run()
    
    file_reader = FileReader(argument_parser.input)
    text_processor = TextProcessor()
    
    lines = file_reader.read_all_lines()
    preprocessed_lines = text_processor.preprocess(lines)
    words = text_processor.split_into_words(preprocessed_lines)



if __name__ == "__main__":
    main()
    
    