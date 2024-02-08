from openai import OpenAI

client = OpenAI()

response = client.Chat.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a highly knowledgeable assistant capable of understanding and annotating instances of obstruction in international negotiations."
        },
        {
            "role": "user",
            "content": "Let us proceed step by step. A) Please learn the following definition of "obstruction" in international negotiations. "Obstruction are of seven types. 1) Parallel Progress:	the delegation repeatedly and openly threatens to block progress on an item it is less concerned about, if insufficient progress is made on another issue that it does care about,.
2) Repetition and Propagation: repeatedly proposing new agenda items on the matter and continuously invoking the issue under other agenda items. 
3) Postponement and Delay: trying to postpone actual decisions
4) Refusal: to Negotiate: refusing to negotiate, invoking (unlikely) excuses. 
5) Holding Out: 	Refusing to join the consensus, either alone or with a small number of supporters—for as long as possible.
6) Exploiting Coalitional Position:	Taking advantage of a specific position in a coalition, such as G-77 coordinator.
7) Procedural Blockage:	invoking procedural rules to delay the negotiations, crossing the fine line that exists between lodging genuinely held concerns over procedural issues in good faith, and deliberately using fine print to frustrate the negotiation process. " 

Do not comment on this task.

B) Your task is to annotate "obstruction" as defined here when found in a series text describing international negotiations. For the following paragraph, return a csv table with two columns: 1st column: "no obstruction" if no obstruction is found ; "obstruction" if one at least is found ; 2nd column "NA" if no obstruction is found ; the names of the countries, if some obstructions are found.
Do not comment on this task.

C) Here are examples of annotation:

“"Chair Roméro asked delegates not to reopen discussions on unbracketed text in subsequent discussions. The EU, US and JAPAN supported this proposal, while SAUDI ARABIA and VENEZULA opposed it. SAUDI ARABIA rejected the Chair’s proposal to establish a Friends of the Chair group to develop compromise text, and threatened to withdraw support for a similar proposal in the contact group on mechanisms. The contact group will reconvene on Wednesday.", obstruction, “Saudi Arabia, Venezuela” 
“COSTA RICA described its proposal for a Copenhagen Protocol and supported a legally-binding agreement.”, no obstruction, NA
“INDONESIA emphasized the importance of making benefit assessments, not just cost assessments, of the Protocol. He called for the Protocol's entry into force by 2002. SWITZERLAND, JAPAN and the NETHERLANDS urged Parties not to wait for ratification before starting to implement actions to address climate change.”, no obstruction, NA
“Negotiations on the draft decision on policies and measures, meanwhile, were almost completely polarized. Developed countries tried to insert a provision allowing voluntary information exchange on developing country P&Ms, and developing countries insisted on a heavy emphasis on the need to minimize the adverse effects of P&Ms. The G-77/China refused to negotiate after a time, citing a lack of progress in negotiations on Protocol Article 2.3. Unwilling to concede on adverse effects, developed countries allowed consideration of P&Ms to be deferred to COP-9.”, obstruction, “g77, China”


C) Annotate the following paragraph."
        }
    ],
    temperature=1,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
