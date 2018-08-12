# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

all_texts = ["'There won't be a trade war,' said the president at the signing ceremony to impose the tariffs –which will be 30 percent on imported solar panels and solar cells and 20 percent on large residential washing machines - regarding potential responses on the part of US trade partners such as South Korea and China.",
             "'Our action today helps to create jobs in America for Americans,' Mr. Trump declared as he imposed tariffs on solar cells and washing machines.",
             "At the World Economic Forum in Davos last week, Trump launched a thinly veiled attack on China, criticising countries with 'predatory' trade practices 'The United States will no longer turn a blind eye to unfair economic practices including massive intellectual property theft, industrial subsidies and pervasive state-led economic planning,' he said",    
             "Trump heightened the trade rhetoric over the weekend, telling Good Morning Britain on Jan. 28 that he has 'a lot of problems with the European Union' that 'may morph into something very big' from 'a trade standpoint,' according to media reports.", 
             "'I want to keep prices down, but I also want to make sure that we have a steel industry and an aluminum industry, and we do need that for national defense,' Trump said.",
             "In a meeting with members of Congress earlier this week, Trump made it clear he is considering implementing the tariffs, saying, 'You may have a higher price (of products) ... but you're going to have jobs.'",
             "At the end of 2017 Trump warned that he would be taking tough measures on China who he sees as an existential economic threat on his country, 'We are declaring that America is in the game and America is going to win'. At that point Trump had done more talking than actually doing anything to impact trade with China.",
             "'Now they're talking about opening up many of them, reopening plants that have been closed for a long time,' Trump said.",
             "'Were going to build our steel industry back and our aluminum industry back,' he said. of the tariffs drove the stocks of U.S. domestic steel and aluminum makers sharply higher, but also hit sentiment on Wall Street due to the potential impact of higher costs on consumers.",
             "'When a country (NYSE: USA ) is losing many billions of dollars on trade with virtually every country it does business with, trade wars are good, and easy to win,' Trump says, in part.",
             "'Gary has been my chief economic advisor and did a superb job in driving our agenda, helping to deliver historic tax cuts and reforms and unleashing the American economy once again,' Trump said.",
             "Mr Trump has previously tweeted 'trade wars are good, and easy to win,' but US Treasury Secretary Steven Mnuchin recently said the president 'was not trying to start a trade war'.",
             "Mnuchin said Trump's over-riding priority is to boost U.S. growth, and that 'economic growth in the U.S. is obviously good for the rest of the world,' he said.",
             "'Many countries are very good at the rhetoric of free trade but in fact actually practice extreme protectionism,' Ross said.",
             "At the end of the fourth round of NAFTA renegotiation talks last year, Lighthizer said USTR had not done 'any analysis' of what an end to the deal would mean for the U.S. 'You always think about what might happen, but we haven't done any analysis of that at this point,' Lighthizer said on Oct. 17, adding, 'we don't really have a plan beyond trying to get a good agreement.' -- Anshu Siripurapu and Jenny Leonard", 
             "Ross also recommends an appeals process 'by which affected U.S. parties could seek an exclusion from the tariff or quota imposed,' both reports state.",        
             "'We have to reduce the deficit, and that will ultimately put pressure on wages and raise wages,' Lighthizer said earlier this week on the Laura Ingraham show, calling it 'nonsense' that the administration was preparing to start a trade war with China.",
             "'Economic strength is military strength,' Ross said, stressing the president is right on that, and noted that countries threatening retaliation would need to find substitutes if they cut of U.S. imports, which could actually hurt their economies..",
             "'I notified the President that today I am beginning an investigation under Section 301 of the Trade Act of 1974,' Lighthizer said."]
analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))
    

analyser.
print_sentiment_scores("Trade War is good")
