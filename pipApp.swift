//
//  pipApp.swift
//  pip
//
//  Created by Fabi Campanari on 23/08/23.
//

import SwiftUI

@main
struct pipApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: pipDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
