class Solution:
    def interpret(self, command: str) -> str:
        # reference the rules given into dictionary
        reference={'G':'G','()':'o','(al)':'al'}
        message=''
        char=''

        for i in command:
            char=char+i
            if char in reference.keys():
                # append the character if it is in reference
                message+=reference[char]
                char=''
        return message

            
