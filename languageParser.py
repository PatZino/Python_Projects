GRAMMAR = '''
    @@grammar::Calc
    start = E $ ;
    E 
        =
        | E '^' A
        | A
        ;
    A
        =
        | A '/' B
        | A '*' B
        | A '+' B
        | A '-' B
        | Ops B
        | B
        ;
    B
        =
        | '('E')'
        | id
        | digit
        ;
    Ops = /-/;
    id = /\w+/;
    digit = /\d+/ ;
'''

def main(sen):
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    ast = parse(GRAMMAR, sen)
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=30)
    print()
    print('JSON VALUE')
    print('odedoyin matthew')
    print(json.dumps(asjson(ast), indent=2))
    print()


sentence = input("STATE THE EXPRESSION TO PARSE: ")
if __name__ == '__main__':
    main(sentence)





