//
//  main.swift
//  SwiftNeuralNetworkGame
//
//  Created by Win Myo Htet on 5/21/16.
//  Copyright © 2016 Win Myo Htet. All rights reserved.
//

import Foundation
//import Surge

func input() -> String {
    let keyboard = NSFileHandle.fileHandleWithStandardInput()
    let inputData = keyboard.availableData
    return NSString(data: inputData, encoding: NSUTF8StringEncoding) as! String
}

//MMM.generateTraingData()
func test(){
    
    let uint32 : UInt32 = 5
    var double : Double = Double(uint32)
    double += 0.4454
    print("\(double)")
   // uint32 = UInt32(roundUpFrom(double,places: 3))
    print("\(uint32)")
}

func fibonacci(size :Int){
    var temp = [Int](count: size, repeatedValue:1)
    (2..<size).map{temp[$0] = temp[$0 - 1] + temp[$0 - 2 ]}
    print("\(temp)")
}

func testNot(){
    print("Starting ...")
    let trainingData = MMM.getTrainingData()
    let massagedData = NN.massageTrainingData(trainingData)
    let coded = massagedData[0]
    print("\(coded)")
    let inputStr = NN.unicodeIntArrayToString(NN.doubleArrayToUnicodeIntArray(coded.0))
    let outputStr = NN.unicodeIntArrayToString(NN.doubleArrayToUnicodeIntArray(coded.2))
    print("\(inputStr) \(outputStr)")
}

//fibonacci(13)
// testNot()
var mmm = MMM()
mmm.setup()
mmm.printBoardSet()
func loop(){
    print("Please enter your input.. or \"q\" to quit")
    var theInput = input()
    if(theInput != "q\n"){
        theInput = String(theInput.characters.dropLast())
        let output = mmm.inputOutput(theInput)
        print("\(output)")
        loop()
    }
}
// loop()
mmm.printStat()
// MMM.createAllDifferentAttributeSolutions()

MMM.createControlledAttributSolutions(1)

/*
 
 //let intArray = theInput.characters.split {$0 == " "}.map(String.init).map { Int($0)!}
 //print("\(intArray)")
 let strArray = theInput.characters.split {$0 == " "}.map(String.init)
 
 //print("\()")
 //print("\(strArray)")
 let intArray:[Int]
 do{
 intArray = strArray.map { Int($0)!}
 }catch{
 print("Error ")
 intArray = []
 }
 //print("\(intArray)")
 if mmm.checkSet(intArray) {
 mmm.updateBoard(intArray)
 mmm.printBoardSet()
 mmm.createSolutionSetFromBoard()
 print("It is a set")
 mmm.printStat()
 }else {
 print("It is not a set \(mmm.boardSetString)")
 }
 */


class HelloWorldPrint{
    func doTheJob(){
        print("Hello World!!!")
    }
}

func someFunc(){
    let helloworld = HelloWorldPrint()
    helloworld.doTheJob()
}


//someFunc()
