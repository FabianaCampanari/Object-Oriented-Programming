//
//  ContentView.swift
//  pip
//
//  Created by Fabi Campanari on 23/08/23.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: pipDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(pipDocument()))
    }
}
