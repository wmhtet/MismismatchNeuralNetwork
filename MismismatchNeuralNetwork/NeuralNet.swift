//
//  NeuralNet.swift
//  SwiftNeuralNetworkGame
//
//  Created by Win Myo Htet on 5/27/16.
//  Copyright © 2016 Win Myo Htet. All rights reserved.
//

import Foundation

class NN{
    static let NUMBER_OF_DECIMAL_PLACES = 5
    
    static func massageTrainingData(trainingData : [(String, String)]) ->
        [(inputUnicodeData:[Double],inputDataMaxLength:Int, outputUnicodeData:[Double],outputDataMaxLength:Int)]{
            var resultData :[(inputUnicodeData:[Double],inputDataMaxLength:Int, outputUnicodeData:[Double],outputDataMaxLength:Int)] = []
            for training in trainingData {
                var result:(inputUnicodeData:[Double],inputDataMaxLength:Int, outputUnicodeData:[Double],outputDataMaxLength:Int) = ([],0,[],0)
                let input = stringToUnicodeIntArray(training.0)
                result.inputUnicodeData = input.map{Double($0)}
                result.inputDataMaxLength = input.count > result.inputDataMaxLength ? input.count : result.inputDataMaxLength
                
                let output = stringToUnicodeIntArray(training.1)
                result.outputUnicodeData = output.map{Double($0)}
                result.outputDataMaxLength = output.count > result.outputDataMaxLength ? output.count : result.outputDataMaxLength
                resultData.append(result)
            }
            return resultData
    }
    
    static func stringToUnicodeIntArray(str:String)->[UInt32]{
        return str.characters.map{String($0)}.map{$0.unicodeScalars}.map{$0[$0.startIndex].value}
    }
    
    static func unicodeIntArrayToString(intArray:[UInt32])->String{
        return intArray.map{UnicodeScalar($0)}.map{Character($0)}.map{String.init($0)}.joinWithSeparator("")
    }
    
    static func doubleArrayToUnicodeIntArray(values:[Double])->[UInt32]{
        return doubleArrayToUnicodeIntArray(values, places: NN.NUMBER_OF_DECIMAL_PLACES)
    }
    
    static func doubleArrayToUnicodeIntArray(values:[Double], places:Int)->[UInt32]{
        return values.map{NN.roundUpFrom($0, places: places)}.map{UInt32($0)}
    }
    
    static func roundUpFrom(value:Double, places:Int )->Double{
        var temp = value
        for place in (0..<places).reverse(){
            temp = roundToPlace(temp, place: place)
        }
        return temp
    }
    
    static func roundToPlace(value:Double, place:Int) -> Double {
        let divisor = pow(10.0, Double(place))
        return round(value * divisor) / divisor
    }
}
