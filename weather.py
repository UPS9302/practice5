import requests as r 
def trivia():
    url="https://opentdb.com/api.php?amount=10"
    response=r.get(url)
    k=0
    if response.status_code==200:
        data=response.json()
        for i in data['results']:
            print(i['question'])
            l=i['incorrect_answers']+[i['correct_answer']]
            print(l)
            input_answer=int(input("enter answer:"))
            if i['correct_answer']==l[(input_answer)-1]:
                k=k+1
                print('score:', k)
    else:
        print("some error occured")
    print("final Score:", k)
if __name__=="__main__":
    trivia()