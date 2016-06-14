//
//  MisMisMatch.swift
//  SwiftNeuralNetworkGame
//
//  Created by Win Myo Htet on 5/21/16.
//  Copyright © 2016 Win Myo Htet. All rights reserved.
//

import Foundation

class MMM{
    static var ENABLE_LOG = false
    private static let NUMBERS = ["1","2","3"]
    private static let SHAPES = ["R","O","D"]
    private static let COLORS = ["R","G","B"]
    private static let FILLINGS = ["E","S","L"]
    private static let TOTAL_CARDS_NUMBERS = 81
    private static let ROW = 4
    private static let COLUMN = 3
    private static let BOARD_SIZE = 12
    private static let TRAINING_DATA_FILE_NAME = "MMM_NN_TRAING_DATA"
    private static let TRAINING_SIZE = 30000
    private static let CARDS:[String] = {
        return MMM.createCards()
    }()
    
    private static let SOLUTIONS : Set<Set<String>> = {
        return MMM.createSolutions()
    }()
    
    private var boardSet = Array(count : MMM.BOARD_SIZE, repeatedValue : -1){
        didSet {
            boardSetUpdateDivisibleBy3 += 1
            //log("boardSet has called didSet \(boardSetUpdateDivisibleBy3)")
        }
    }
    private var boardSolutionSet = Set<Set<Int>>()
    private var boardSetUpdateDivisibleBy3 = 0
    private var numberOfAttempts = 0
    private var numberOfCorrectAttempts = 0
    var boardSetString:String {
        get{
            return getBoardSet()
        }
    }
    private static func createCards()->[String]{
        var cards:[String] = []
        for number in NUMBERS{
            for shape in SHAPES{
                for color in COLORS{
                    for filling in FILLINGS{
                        cards.append(number + shape + color + filling)
                    }
                }
            }
        }
        return cards
    }
    
    private static func createSolutions() -> Set<Set<String>> {
        var solutionSet = Set<Set<String>>()
        
        func isSet(firstCard:String, secondCard:String, thridCard:String) -> Bool {
            func isValid(pos:Int) -> Bool {
                let firstCh = String(firstCard[firstCard.startIndex.advancedBy(pos)])
                let secondCh = String(secondCard[secondCard.startIndex.advancedBy(pos)])
                let thirdCh = String(thridCard[thridCard.startIndex.advancedBy(pos)])
                
                var count = 0
                if(firstCh == secondCh) {
                    count += 1
                }
                
                if(secondCh == thirdCh){
                    count += 1
                }
                
                if(firstCh == thirdCh) {
                    count += 1
                }
                return (count == 0 || count == 3)
            }
            
            if(!isValid(0)){
                return false
            }
            if(!isValid(1)){
                return false
            }
            if(!isValid(2)){
                return false
            }
            if(!isValid(3)){
                return false
            }
            return true
        }
        
        for firstCard in CARDS{
            for secondCard in CARDS{
                for thirdCard in CARDS{
                    
                    if (firstCard != secondCard && secondCard != thirdCard && firstCard != thirdCard) {
                        if(isSet(firstCard,secondCard: secondCard,thridCard: thirdCard)){
                            solutionSet.insert(Set(arrayLiteral: firstCard, secondCard, thirdCard))
                        }
                    }
                }
            }
        }
        return solutionSet
    }
    
    func checkSet(posList: [Int]) -> Bool{
        numberOfAttempts += 1
        if posList.count != 3 {return false}
        //let array = [MMM.CARDS[boardSet[posList[0]]],MMM.CARDS[boardSet[posList[1]]],MMM.CARDS[boardSet[posList[2]]]]
        //log("\()")
        //log("\(array)")
        let answerSet = Set(posList)
        let set = Set(answerSet)
        return boardSolutionSet.contains(set)
    }
    
    func setup(){
        let range = Array(0..<MMM.BOARD_SIZE)
        boardSetUpdateDivisibleBy3 -= 12
        numberOfCorrectAttempts -= 1
        updateBoard(range)
        printBoardSet()
        createSolutionSetFromBoard()
    }
    
    func createSolutionSetFromBoard(){
        numberOfCorrectAttempts += 1
        boardSolutionSet = Set<Set<Int>>()
        for first in 0..<MMM.BOARD_SIZE{
            for second in 0..<MMM.BOARD_SIZE{
                for third in 0..<MMM.BOARD_SIZE{
                    if (first != second && second != third && first != third) {
                        let firstCard = boardSet[first]
                        let secondCard = boardSet[second]
                        let thirdCard = boardSet[third]
                        let set = Set(arrayLiteral: MMM.CARDS[firstCard],MMM.CARDS[secondCard],MMM.CARDS[thirdCard])
                        
                        if(MMM.SOLUTIONS.contains(set)){
                            let answerSet = Set<Int>(arrayLiteral: first,second,third)
                            boardSolutionSet.insert(answerSet)
                            //log(":\(MMM.CARDS[firstCard]) \(MMM.CARDS[secondCard]) \(MMM.CARDS[thirdCard])")
                            //log("\(first) \(second) \(third) ")
                        }
                    }
                }
            }
        }
        log("\(boardSolutionSet)")
        if(boardSolutionSet.count == 0){
            log("No solution. Running it again.")
            setup()
        }
    }
    
    func updateBoard(posList: [Int]){
        var currentSet = Set(boardSet)
        
        func generateRandomnumber() -> Int {
            let random = Int(arc4random_uniform(UInt32(MMM.TOTAL_CARDS_NUMBERS)))
            if(currentSet.contains(random)){
                return generateRandomnumber()
            }
            return random
        }
        
        for pos in posList {
            if (0..<MMM.BOARD_SIZE ~= pos ){
                let generated = generateRandomnumber()
                boardSet[pos] = generated
                currentSet.insert(generated)
            }
        }
    }
    
    func printBoardSet(){
        for pos in 0..<MMM.BOARD_SIZE {
            let terminator = ( pos % MMM.COLUMN == 2 ) ? "\n" : ""
            let cardPos = boardSet[pos]
            if (0..<MMM.TOTAL_CARDS_NUMBERS ~= cardPos ){
                log("\(MMM.CARDS[cardPos]) " , terminator:terminator)
            }
        }
    }
    
    func inputOutput(input:String)-> String{
        let intArray: [Int]
        do {
            intArray = try getIntArray(input, delimiter: " ")
        }catch let error as NSError {
            //print(error)
            intArray = []
        }
        if checkSet(intArray) {
            updateBoard(intArray)
            printBoardSet()
            createSolutionSetFromBoard()
            log("It is a set")
            printStat()
        }else{
            log("It is not a set ")
        }
        return getBoardSet()
    }
    
    func getIntArray(input:String, delimiter:Character ) throws -> [Int] {
        let strArray = input.characters.split {$0 == delimiter}.map(String.init)
        let intArray = try strArray.map {
            (int:String)->Int in
            guard Int(int) != nil else {
                throw NSError.init(domain:  " \(int) is not digit", code: -99, userInfo: nil)
            }
            return Int(int)!
        }
        return intArray
    }
    
    func getBoardSet()->String{
        var str = ""
        for pos in 0..<MMM.BOARD_SIZE {
            let cardPos = boardSet[pos]
            str += "\(MMM.CARDS[cardPos]) "
        }
        return String(str.characters.dropLast())
    }
    
    func printStat() {
        print("numberOfCorrectAttempts: \(numberOfCorrectAttempts) numberOfAttempts: \(numberOfAttempts) boardSetUpdateDivisibleBy3: \(boardSetUpdateDivisibleBy3) ")
    }
    
    private func log(str:String){
        log(str, terminator: "\n")
    }
    
    private func log(str:String, terminator:String){
        if(MMM.ENABLE_LOG){
            print(str, terminator:terminator)
        }
    }
    
    static func generateTraingData(){
        if let dir = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.AllDomainsMask, true).first {
            let path = NSURL(fileURLWithPath: dir).URLByAppendingPathComponent(MMM.TRAINING_DATA_FILE_NAME)
            generateTraingData(path)
        }else {
            print("No User's Documents?")
        }
    }
    
    static func generateTraingData(path : NSURL){
        let mmm = MMM()
        
        func createInputOutputString( board:String, solutions:Set<Set<Int>>)->String{
            var str = ""
            for solution in solutions{
                //var array = Array()
                let solutionArray = solution.map{$0.description}.joinWithSeparator(" ")
                str += "\(board):\(solutionArray)\n"
            }
            return str
        }
        
        func repeatGettingSolution()->String{
            var str = ""
            for i in 1...MMM.TRAINING_SIZE {
                if i%1000 == 0{
                    print(".", terminator:"")
                }
                mmm.setup()
                str += createInputOutputString( mmm.getBoardSet(), solutions:mmm.boardSolutionSet)
            }
            print("")
            return str
        }
        
        let text = repeatGettingSolution()
        
        //writing
        do {
            try text.writeToURL(path, atomically: false, encoding: NSUTF8StringEncoding)
        }catch {
            /* error handling here */
            print("Error writing file \(path).")
        }
    }
    
    static func readTraingData()->[(String, String)]{
        if let dir = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.AllDomainsMask, true).first {
            let path = NSURL(fileURLWithPath: dir).URLByAppendingPathComponent(MMM.TRAINING_DATA_FILE_NAME)
            return readTraingData(path)
        } else {
            print("No User's Documents?")
            return []
        }
    }
    
    static func readTraingData(path : NSURL)->[(String, String)]{
        var solutions:[(String, String)] = []
        
        //reading
        do {
            let text2 = try NSString(contentsOfURL: path, encoding: NSUTF8StringEncoding) as String
            let strArry = text2.characters.split {$0 == "\n"}.map(String.init)
            for str in strArry {
                var tmp = str.characters.split{$0 == ":"}.map(String.init)
                solutions.append(( String(tmp[0].characters), String(tmp[1].characters)))
            }
            //print("\(solutions)")
        }catch {
            /* error handling here */
            print("Error reading file \(path).")
        }
        return solutions
        
    }
    
    static func getTrainingData()->[(String, String)]{
        if let dir = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.AllDomainsMask, true).first {
            if (!NSFileManager.defaultManager().fileExistsAtPath(dir+"/\(MMM.TRAINING_DATA_FILE_NAME)")){
                generateTraingData()
            }
        }
        return readTraingData()
    }
}
