package com.raphtory.mastodon;

import com.raphtory.mastodon.graphbuilders.MastUserGraphBuilder
import com.raphtory.core.build.server.RaphtoryGraph
import com.raphtory.algorithms.{ConnectedComponents, Degree}
import com.raphtory.spouts.FileSpout


object Runner extends App{
        val source    = new FileSpout("src/main/scala/com/raphtory/mastodon/data","tfg2.csv")
        val builder   = new MastUserGraphBuilder()
        val rg        = RaphtoryGraph[String](source,builder)
        rg.rangeQuery(Degree(path="/tmp/deg"), start = 1482404531000L, end = 1525723247000L, increment = 31536000000L, windows = List( 31536000000L))
        }