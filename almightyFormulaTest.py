GRAMMAR = '''
    @@grammar::Calc
    start = expression $ ;
    expression 
        =
        | expression '/' term
        | expression '+' term
        | expression '-' term
        | expression '**' term
        | term
        ;
    term
        =
        | term '*' factor
        | term '+' factor
        | term '-' factor
        | term '/' factor
        | sign factor
        | factor
        ;
    factor
        =
        | '('expression')'
        | number
        | identifier
        ;
    sign = /-/;
    number = /\d+/ ;
    identifier = /\w+/;
'''


def main():
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    ast = parse(GRAMMAR, '(-b + ((b * b) - (4 * a * c)) ** (1/2)) / (2 * a)')
    #  ast = parse(GRAMMAR, '-b')
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()
    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()


if __name__ == '__main__':
    main()





