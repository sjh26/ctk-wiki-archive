---
title: Documentation/CTK Plugin EventAdmin local
---

1. Description
The Event Admin Service Specification (part of the OSGi Compendium specification) defines a general inter-plugin communication mechanism. The communication can be performed synchronously or asynchronously and uses a publish/subscribe pattern.

The main components in a publish/subscribe communication are:

- Event Publisher - sends events or messages related to a specific topic
- Event Handler (or Subscriber) - expresses interest in one or more topics and receives all the messages belonging to such topics.

Events are composed of two attributes:

- A topic defining the nature of the event; topic names are usually arranged in a hierarchical namespace, where slashes are used to separate the levels (i.e. "org/commontk/PluginFrameworkEvent/STARTED")
- A set of properties describing the event.

      1. Features
The CommonTK Event Admin implementation in *org.commontk.eventadmin* is based on the implementation of the Event Admin specs in the Apache Felix project and provides in-process communication. It exhibits a similar set of features as the Apache Felix implementaion:

- Try to deliver events as fast as possible
- Events sent from different threads are sent in parallel.
- Events from the same thread are sent in the order they are received (this is according to the spec).
- A timeout can be configured which is used for event handlers. If an event handler takes longer than the configured timeout to process an event, it is blacklisted. Once a handler is in a blacklist, it doesn't get sent any events anymore.

      1. Tutorials
- [Introduction](http://www.commontk.org/docs/html/PluginFramework_EventAdmin_Page.html)