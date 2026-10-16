# Maya 4.0 — One-time Add-on Upgrade (Android phone only)

**What this is:** This ZIP is the upgrade kit for your *existing* public `tanimgaming31-ops/Maya2.2` GitHub repository. It is not an APK by itself. It keeps the current `index.html`, `maya.vrm`, Gemini integration, Memory, Messenger/imo/Instagram Android notification bridge and design. Do **not** delete any existing files.

## Install from an Android phone — exactly one upgrade run

1. Download and extract the ZIP with Files by Google / Android Files.
2. Open **https://github.com/tanimgaming31-ops/Maya2.2** in Chrome, logged in.
3. At the repository root choose **… > Upload file**, and select these **three files from the extracted ZIP**:
   - `maya4.js`
   - `maya4.css`
   - `maya4_install.py`
   Commit these to branch `main`. Do not upload the ZIP itself as an app file.
4. Return to the repository. Open the existing `.github/workflows` folder. Choose **… > Upload file**, select the `maya4-install.yml` file from the *root of the extracted ZIP*, and commit. (Do not upload it to the repository root; it belongs inside `.github/workflows/`.)
5. Tap **Actions → Install and Build Maya 4 APK → Run workflow → Run workflow**. Wait for a green check. One run does all of this:
   - Backs up your exact current `index.html` as `index-before-maya4.html`.
   - Adds the new add-on panel and approximate expression/viseme enhancements, without replacing your original Gemini/VRM code.
   - Bundles `maya.vrm` (if it exists) and Maya 4 modules into the Android APK.
   - Builds a new `Maya-4.apk`.
   - Only after the APK builds successfully, commits the updated `index.html`/`sw.js` to the repository.
   - Publishes `Maya-4.apk` as a GitHub Release and an Actions Artifact.
6. Download `Maya-4.apk` from that successful workflow's **Artifacts** or from the newest **Release**. The Android app ID stays `com.tanim.maya2`, separate from the old `com.tanim.maya`.
7. Open Maya, and tap the **M4** circle near the upper buttons to access the new tools. Your original Android build workflow is unchanged; for future Maya 4 APK builds, run **Install and Build Maya 4 APK** again.

**If the workflow cannot push the source changes because of GitHub repository write permissions:** the APK Artifact should still be available after a successful compile; enable Actions read/write access in the repository or perform the small index update manually. The APK's features depend on permissions and device support.

### New add-on tools and exact limits

| Feature | What really works | What is not promised |
| --- | --- | --- |
| 3D eye/face/lips | Existing VRM blink, head, chest, A/I/U/E/O expressions; new approximate caption-aware vowel mapping when output captions are present | Perfect word/phoneme synchronization or photorealistic reconstruction of the original photo |
| Emotional voice | Choice of gentle/calm/playful/focused Gemini prompt style on **new** calls | Independently engineered emotion voice synthesis or guaranteed natural audio |
| Memory 3 | Timeline of existing memories, pinned memories, search, export without API key | Cloud sync or automatic perfect semantic memory |
| Screen vision | One-time permission-based screen capture **if the browser supports it**, or choose a screenshot/image; send to Gemini only after consent | Continuous reading of other apps' private screens or Android MediaProjection without native service |
| PDF | Extract text from first 25 pages locally using pdf.js via internet CDN; optional Gemini explanation | OCR of scanned PDF pages (use an image), offline PDF.js installation |
| Reminders | Local app-open reminder alerts, Calendar event link for background alerts | Native reliable alerts with app fully closed without saving a Calendar event |
| Daily briefing | User-triggered Gemini briefing; requests Google Search grounding where available | Guaranteed current weather/news without grounding or a paid API quota |
| Messaging | Show recent supported Android notifications; optional Quick Reply if a notification supports it, with confirmation | Reading all old Messenger/imo/Instagram chats or sending any private message secretly |
| Offline Phone Commands | Typed commands for torch, volume, brightness, music and launching installed apps inside Android APK | Freeform offline speech recognition or control of every app screen |
| 3D colors | Change named compatible VRM material colors, restore original colors; emotion buttons | Automatically fitting new clothes/hair geometry to every VRM; needs separate rigged asset |
| Translator & tutor | Gemini translation/correction; device TTS of a result if available | Free guaranteed speech translation without internet |

### Important privacy and hardware behavior

- Google Gemini API key remains stored only under the app's existing on-device key, not uploaded to GitHub.
- When you tap **Ask Gemini** for screenshot, picture, PDF, or translation, that selected content is sent **directly to Google** using your key.
- Phone-message access requires Android Notification Access; it is limited to notifications exposed by Android and supported RemoteInput reply actions.
- The `maya.vrm` model currently in your repository is kept as-is, not bundled in this ZIP. If its permission/license forbids public hosting, do not publish it.
- Native 3D in the APK requires WebGL/Three.js. At first load Three.js currently uses the public CDN, so internet is required to fetch the rendering library unless already cached.
- Screen capture on Chrome Android/Android WebView may be unsupported. Use Android's normal Screenshot feature and import the image instead.
- This repository currently has no verified native background screen reader. Android MediaProjection requires explicit consent and foreground service permissions.
- Notification reading, microphone, screenshots, and replying always require appropriate permission and, for outgoing replies, user confirmation.

### Testing and status

- `node --check maya4.js`: **passed**.
- `python -m py_compile maya4_install.py`: **passed**.
- Browser test (Chromium, mock in-memory localStorage) verified all 8 tabs, existing memory pins, reminder storage, voice style controls, disabled native-action warning, avatar safe fallback: **passed**.
- Python installer tested against an earlier Maya 3.1 backup. The current live repo's VRM code was inspected for the anchors, but **full patch + latest APK build on GitHub and real Android phone were not performed in this environment**.
- A green GitHub Actions check means only that compilation succeeded, not that all phone features work. Test one by one on your phone.

**Do not upload this ZIP as a whole to GitHub in place of the source, and do not delete the original `index.html` or `maya.vrm`.**
