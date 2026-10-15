# Maya source inspection

The original `index.html` was preserved structurally with only the new Android background-listening UI and lifecycle fixes; all existing features remain in source.

Automatable checks without network or Android SDK:
- `bash -n setup-native.sh`
- extract inline `<script>` from `index.html`, then `node --check` the extracted JavaScript
- run `setup-native.sh` against a mock Capacitor AndroidManifest.xml/build.gradle, then parse the manifest with XML parser
- check the generated native classes and permissions exist.

NOT verified here: Android Gradle compilation, Android 16 voice recognition and microphone-FGS behavior, Gemini API, message Quick Reply on a physical phone, APK installation/signature matching, GitHub build run. These require a connected GitHub repository, Android SDK and real device/API key.

Separate app variant: appId com.tanim.maya2; appName Maya 2. Built as a separate Android package. APK compilation NOT verified.
