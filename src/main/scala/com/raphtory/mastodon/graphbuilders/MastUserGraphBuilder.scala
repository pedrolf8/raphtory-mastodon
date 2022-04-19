package com.raphtory.mastodon.graphbuilders


import com.raphtory.core.components.graphbuilder.GraphBuilder
import com.raphtory.core.implementations.generic.messaging._
import com.raphtory.core.model.graph.{ImmutableProperty, Properties, Type}


import java.text.SimpleDateFormat


class MastUserGraphBuilder extends GraphBuilder[String]{
    
    override def parseTuple(tuple: String) = {
        val fileLine = tuple.split(";").map(_.trim)
        val sourceNode = fileLine(1).toInt
        /*val targetNode = fileLine(2).toInt
        val targetNoderep = fileLine(2).toInt*/
        val targetNodement1 = fileLine(3).toInt
        val targetNodement2 = fileLine(4).toInt
        val targetNodement3 = fileLine(5).toInt
        val targetNodement4 = fileLine(6).toInt
        val targetNodement5 = fileLine(7).toInt
        val targetNodement6 = fileLine(8).toInt
        val targetNodement7 = fileLine(9).toInt
        val targetNodement8 = fileLine(10).toInt
        val targetNodement9 = fileLine(11).toInt
        val targetNodement10 = fileLine(12).toInt
        /*
        if (targetNode > 0 && targetNode != sourceNode) {
            val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 19))
            addVertex(creationDate, sourceNode, Type("User"))
            addVertex(creationDate, targetNode, Type("User"))
            addEdge(creationDate, sourceNode, targetNode, Type("User to User"))
        }*/
            if (targetNodement1 > 0 && targetNodement1 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement1, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement1, Type("User to User"))
            }
            if (targetNodement2 > 0 && targetNodement2 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement2, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement2, Type("User to User"))
            }
            if (targetNodement3 > 0 && targetNodement3 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement3, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement3, Type("User to User"))
            }
            if (targetNodement4 > 0 && targetNodement4 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement4, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement4, Type("User to User"))
            }
            if (targetNodement5 > 0 && targetNodement5 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement5, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement5, Type("User to User"))
            }
            if (targetNodement6 > 0 && targetNodement6 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement6, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement6, Type("User to User"))
            }
            if (targetNodement7 > 0 && targetNodement7 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement7, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement7, Type("User to User"))
            }
            if (targetNodement8 > 0 && targetNodement8 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement8, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement8, Type("User to User"))
            }
            if (targetNodement9 > 0 && targetNodement9 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement9, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement9, Type("User to User"))
            }
            
            
            if (targetNodement10 > 0 && targetNodement10 != sourceNode) {
                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))
                addVertex(creationDate, sourceNode, Type("User"))
                addVertex(creationDate, targetNodement10, Type("User"))
                addEdge(creationDate, sourceNode, targetNodement10, Type("User to User"))
            }
    }

    def dateToUnixTime (timestamp: => String): Long = {
        val sdf   = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")
        val dt    = sdf.parse(timestamp)
        val epoch = dt.getTime
        epoch
    }



}