import sys
import Vertex
import Vocabulary

def main():

    vocabulary = Vocabulary.Vocabulary()

    for w in ['i', 'ie', 'ice', 'ire', 'is', 'isle', 'icy', 'frog', 'ere', 'err', 'erro', 'error']:
        vocabulary.add_vertex(w)

    print "VOCABULARY:"
    print vocabulary

    s = Vertex.Vertex('ire')
    res = vocabulary.bfs(s)
    print "RESULT FOR:", s.value
    print res

if __name__ == "__main__":
    sys.exit(main())
