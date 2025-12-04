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
      // Use your Render URL here
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
      setStory("Error connecting to the server. (The server might be waking up, please try again in 1 minute!)");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-8 bg-blue-50 font-sans text-gray-900">
      <h1 className="text-4xl md:text-6xl font-extrabold text-blue-600 mb-8 tracking-tight drop-shadow-sm text-center">
        ✨ Magic Story Generator ✨
      </h1>
      
      <div className="w-full max-w-2xl mb-6">
        <textarea 
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="e.g. A tiny robot who loves to bake cookies..."
          rows={4}
          className="w-full p-6 rounded-2xl border-2 border-blue-200 shadow-sm text-lg focus:ring-4 focus:ring-blue-300 focus:border-blue-400 outline-none resize-none text-gray-700 transition-all bg-white"
        />
      </div>

      <button 
        onClick={handleGenerate} 
        disabled={loading}
        className={`relative px-10 py-4 text-xl font-bold text-white rounded-full transition-all duration-300 shadow-xl transform ${
          loading 
            ? "bg-blue-400 cursor-wait scale-95" 
            : "bg-blue-600 hover:bg-blue-500 hover:scale-105 hover:shadow-2xl active:scale-95"
        }`}
      >
        <div className="flex items-center gap-3">
          {loading && (
            // This is the Spinner Icon
            <svg className="animate-spin h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          )}
          {loading ? "Creating Magic..." : "Generate Story 🚀"}
        </div>
      </button>

      {story && (
        <div className="mt-10 p-8 bg-white rounded-3xl shadow-xl w-full max-w-3xl border border-blue-100 animate-fade-in-up">
          <h3 className="text-2xl font-bold text-blue-800 mb-4 border-b pb-2 border-blue-100">
            Your Story:
          </h3>
          <div className="prose prose-lg text-gray-600 leading-relaxed whitespace-pre-wrap">
            {story}
          </div>
        </div>
      )}
    </main>
  );
}