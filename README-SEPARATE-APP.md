# Maya 2 — Separate App (Android)

- Original installed app: **Maya** / `com.tanim.maya`
- This new app: **Maya 2** / `com.tanim.maya2`
- They can coexist on the same Android phone. Neither uninstalls the other.
- The Maya 2 app data / Gemini API key / memories are independent from the old package.
- Existing visual UI, character, Gemini features and native-layer source retained.
- The old debug signing key has deliberately NOT been included in this new package.

## Build from Android phone

1. Extract this archive.
2. Create a separate **private** GitHub repository for Maya 2.
3. Upload the **contents** of the `Maya-2-Separate` folder to the repository root, including `.github/workflows/build-apk.yml`. Do not overwrite the older Maya repository.
4. Run **Actions > Build Maya 2 Android APK > Run workflow**.
5. If the workflow succeeds, download `Maya-2.apk` from Artifacts / Releases.
6. Install as a separate app and enter your Gemini API key in Maya 2 settings.

## Limitations

Code was checked for JavaScript and shell syntax, but the Android Gradle build, actual APK installation, Gemini Live call, Notification Quick Reply and background recognition require real verification. Always-on recognition is experimental, explicitly opt-in, microphone foreground-service based, and cannot be guaranteed 24/7.
