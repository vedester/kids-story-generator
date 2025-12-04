'use client';

import { useState } from 'react';

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!prompt) return;
    
    setLoading(true);
    setStory(""); 

    try {
      // Connect to Django Backend
      // local dev
// const response = await fetch('http://127.0.0.1:8000/api/stories/generate/', {
      //production dev
      const response = await fetch('https://kids-story-generator-backend.onrender.com/api/stories/generate/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
      });

      const data = await response.json();
      
      if (data.story) {
        setStory(data.story);
      } else {
        setStory("Something went wrong. Please try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      setStory("Error connecting to the server. Is Django running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-8 bg-gray-50 font-sans text-gray-900">
      <h1 className="text-4xl font-bold text-gray-800 mb-8">
        ✨ Magic Story Generator ✨
      </h1>
      
      <div className="w-full max-w-2xl mb-6">
        <textarea 
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Tell me a story about a cat who learns to fly..."
          rows={4}
          className="w-full p-4 rounded-lg border border-gray-300 shadow-sm text-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none resize-none text-gray-700"
        />
      </div>

      <button 
        onClick={handleGenerate} 
        disabled={loading}
        className={`px-8 py-3 text-lg font-bold text-white rounded-full transition-all duration-300 shadow-lg ${
          loading 
            ? "bg-gray-400 cursor-not-allowed" 
            : "bg-blue-600 hover:bg-blue-700 hover:scale-105"
        }`}
      >
        {loading ? "Writing Story..." : "Generate Story"}
      </button>

      {story && (
        <div className="mt-12 p-8 bg-white rounded-xl shadow-lg w-full max-w-3xl border border-gray-100">
          <h3 className="text-2xl font-semibold text-gray-800 mb-4">Your Story:</h3>
          <p className="whitespace-pre-wrap text-gray-600 leading-relaxed text-lg">
            {story}
          </p>
        </div>
      )}
    </main>
  );
}