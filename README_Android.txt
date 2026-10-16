MAYA VRM VOICE COMPANION — ANDROID PHONE / GITHUB PAGES
====================================================

IMPORTANT: Keep these 4 files together in the SAME GitHub repository folder:
  index.html
  maya.vrm
  manifest.webmanifest
  icon-192.png
  icon-512.png

This package retains the existing Maya voice/chat/memory settings.
Your own VRM sample avatar is included (maya.vrm, ~26 MB).
Model format: VRM 0.0, with humanoid bones and facial blendshapes.

INSTALL USING ANDROID PHONE ONLY:
  1. Open your GitHub Pages repository using Chrome and sign in.
  2. Back up the existing index.html. Keep a copy of your API key separately.
  3. Choose Add file > Upload files (or edit using the repository file manager).
  4. Upload all five files together into the same folder. Commit changes.
     GitHub browser uploading 26 MB can take time on mobile Wi-Fi.
  5. Ensure GitHub Pages is enabled under Settings > Pages and open your HTTPS pages URL.
  6. On first visit, give the 3D model time to download/render.
  7. Settings > Look > Maya VRM (animated 3D). Optional: Test blink / Test talking / Test smile.
  8. Add and test your OWN Gemini API key if needed. The model itself does not require a key to animate in the settings preview.

HOW IT WORKS:
  - Imports VRM 0.0 or GLB from phone Files using Settings > Look > Choose VRM / GLB.
  - Stores your imported model in device IndexedDB if the browser allows it.
  - When no custom import exists, loads maya.vrm from the website alongside index.html.
  - VRM0 expression targets: Blink, Joy and A/I/U/E/O mapped from the actual VRM metadata.
  - Talking mouth varies with audio energy. It is NOT word-perfect phoneme lip-sync.
  - Slight head, chest and hair movement; automatic blinking.
  - Live voice uses online Gemini; browser fallback uses device speechSynthesis if supported.

LIMITATIONS:
  - 3D avatar requires WebGL and free Three.js browser modules loaded via internet.
  - GitHub Pages is an HTTPS host and not the same as opening index.html directly from Files app.
  - This avatar is the VRoid sample you downloaded, not the black/purple butterfly character.
  - No built-in motion clips were found in the VRM; procedural animations are driven in JavaScript.
  - Tested: GLB/VRM metadata integrity, static HTML and JavaScript syntax.
  - NOT verified on your specific Android phone or with a working Gemini call.
  - Your imported model remains on your device unless you choose to upload it publicly.
  - Your included model is publicly available if you put maya.vrm on a public GitHub Pages site;
    check the model's VRoid license before redistributing it.

TROUBLESHOOT:
  - If the avatar doesn't show: ensure maya.vrm exists next to index.html on GitHub Pages, check mobile internet, open Chrome and reload.
  - If blank: Settings > Look > Original cartoon/Reference portrait (2D) until WebGL works.
  - If no talking mouth: Settings > Look > Test talking, then check that audio is actually playing.
  - If you accidentally imported the wrong model: Settings > Look > Remove imported model.
  - You can keep Gemini key and memories by updating the same GitHub Pages origin, not switching site domains or clearing browser storage.
