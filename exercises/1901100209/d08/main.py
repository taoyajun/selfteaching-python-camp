from mymodule import stats_word
import traceback

def test_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('texs_traceback =>',e)
        print(traceback.format_exc())




if __name__ == '__main__':
    test_traceback()