# Maya 2 — পুরোনো Maya থেকে সম্পূর্ণ আলাদা Android অ্যাপ

**এই ZIP-টি পুরোনো Maya-কে Replace বা Update করবে না।** পুরোনো Maya-এর Package ID `com.tanim.maya`, নতুনটির `com.tanim.maya2`। Android Launcher-এ নতুনটির নাম **Maya 2**। একই ফোনে দুটি অ্যাপ পাশাপাশি থাকবে। পুরোনো অ্যাপের ডেটা না মুছে, নতুন অ্যাপে Settings ও API Key আলাদাভাবে বসাও।

**সতর্কতা:** GitHub-এ পুরোনো Maya source overwrite না করে একটি **নতুন Private Repository** খুলে নতুন প্রজেক্ট ফাইলগুলো আপলোড করো। শুধু ZIP আপলোড করলে GitHub Actions APK তৈরি করতে পারবে না।

এই ZIP-এ পুরোনো Maya-র `index.html`-এর UI, Gemini Voice/Text, Memory, Camera, Color Settings বজায় আছে। Android Native Phone Controls, Notification Read/Reply এবং ব্যবহারকারী চালু করতে পারেন এমন **experimental background wake phrase**-এর কোডও আছে। এটি `com.tanim.maya2` অ্যাপ হিসেবে বিল্ড হয়।

## GitHub-এ Android APK বানানো (PC লাগবে না)

1. Android Chrome থেকে github.com-এ লগইন করে নিজের একটি **private repository** তৈরি করো। এই আলাদা অ্যাপ ZIP-এ পুরোনো অ্যাপের signing key দেওয়া হয়নি।
2. এই ZIP extract করে `maya2-main` ফোল্ডারের সব প্রজেক্ট ফাইল ও `.github/workflows/build-apk.yml` GitHub repository-তে একই path রেখে upload/commit করো। শুধু ZIP ফাইল upload করলে workflow চলবে না। `.github` hidden folder-টিও upload করতে হবে।
3. GitHub-এ **Actions** → **Build Maya 2 Android APK** → **Run workflow** → **Run workflow** চাপো। `main`-এ Push করলেও APK build হয়, কিন্তু GitHub Release শুধু manual build-এ তৈরি হবে।
4. Build সবুজ হলে Actions-এর সেই Run-এর **Artifacts**-এ `Maya-2-Android-APK` থেকে APK ZIP ডাউনলোড করে `Maya-2.apk` বের করো। Manual build-এ **Releases**-এও `Maya-2.apk` পাওয়া যাবে।
5. Android-এ Downloads থেকে `Maya-2.apk` চাপো। প্রয়োজন হলে Files/Chrome-এর **Install unknown apps** অনুমতি দাও। ইনস্টল করার পর Maya → Settings → Gemini API Key বসাও ও Test করো।

**আলাদা অ্যাপ:** এটির Package ID `com.tanim.maya2` এবং ফোনে নাম **Maya 2**। পুরোনো `com.tanim.maya` অ্যাপ uninstall বা replace করার প্রয়োজন নেই। দুই অ্যাপের Settings, Local Memory এবং API key আলাদা থাকবে; নতুন অ্যাপে API key আবার বসাতে হবে।

## Android বিশেষ সুবিধা চালু করো

- **মেসেজ পড়া / Quick Reply:** Settings → Messages → Notification access → Allow → Android Settings-এ Maya Enable করো। Android-এর restricted settings বাধা দিলে App info থেকে প্রয়োজনীয় অনুমতি নিজে দিতে হবে। Maya কেবল সমর্থিত অ্যাপের notification text পড়ে, সম্পূর্ণ chat history নয়। রিপ্লাই দেওয়ার আগে ব্যবহারকারীর অনুমতি লাগে; source app Quick Reply সমর্থন না করলে কাজ করবে না।
- **Phone Controls:** মিউজিক/ভলিউম/টর্চের মতো কমান্ড Maya-কে বলো। Brightness বদলাতে Settings → Change brightness → Allow করো। সরাসরি SMS পাঠানোর জন্য Settings → Send SMS → Allow; প্রতিটি SMS-এর জন্য নিশ্চিতকরণ দরকার।
- **Background Listening (Experimental):** Settings → Background listening → **Enable background listening** চাপো, সম্মতি দাও, Android Mic ও Notifications অনুমতি দাও, প্রয়োজন হলে দ্বিতীয়বার Enable চাপো। চলার সময় **Maya 2 · microphone active** নোটিফিকেশন থাকবে। "Hey Maya" বললে শনাক্ত হলে Maya একটি Notification দেবে; **সেখানে ট্যাপ করে** অ্যাপ খুলে মাইক চাপতে হবে। নোটিফিকেশনের **Stop listening** বা Settings-এর Stop দিয়ে বন্ধ করো।

## কী কী সীমাবদ্ধতা আছে

- SpeechRecognizer বারবার চালু করে Wake Phrase খোঁজার ব্যবস্থা **experimental**: Android, speech service, ভাষা, battery optimisation এবং ফোন লক থাকা অবস্থার নিয়ম অনুযায়ী এটি বন্ধ হয়ে যেতে পারে; ২৪/৭ গ্যারান্টি দেওয়া যায় না। এটি hardware-DSP hotword engine নয়। ফোনের reboot-এর পর microphone স্বয়ংক্রিয় চালু হয় না।
- Notification পড়া ও reply করতে Android Notification Listener অনুমতি লাগে। Sender/message শুধু memory (RAM)-এ থাকে; notification মুছে গেলে quick reply আর কাজ নাও করতে পারে। Message text Gemini-তে যাবে কেবল তখনই যখন তোমার নির্দেশে Maya সেগুলো AI কথোপকথনে ব্যবহার করে।
- Background listener Android Speech Recognition provider ব্যবহার করে; ওই provider শব্দ শনাক্ত করতে অডিও প্রক্রিয়াজাত করতে পারে। Live Chat-এর শব্দ Google Gemini-তে যায়। গোপন রেকর্ডিং বা কারও অনুমতি ছাড়া মাইক্রোফোন ব্যবহারের উদ্দেশ্যে নয়।
- Native API/permissions/Camera/Phone features ডিভাইস ও Android version অনুযায়ী আলাদা হতে পারে। GitHub Actions build ও বাস্তব ফোনে APK ইনস্টল এই পরিবেশে যাচাই করা সম্ভব হয়নি।
- GitHub Pages/PWA সংস্করণে Android Native features নেই; শুধু Android APK-তে Native Code যুক্ত হয়।
- এই APK **debug build**—Play Store-এ প্রকাশের release package নয়।

## পরীক্ষা করো

1. Maya খুলে API key Test → text chat → microphone দিয়ে voice call।
2. Settings → notification access Allow → অন্য ফোন থেকে WhatsApp message পাঠাও → Maya-কে বলো নতুন message পড়তে।
3. Reply চাইলে Maya Confirmation-এ অনুমতি দিয়ে Quick Reply পরীক্ষা করো।
4. Torch, music pause/play, volume, brightness permission, alarm, SMS (শুধু নিজের নম্বরে) পরীক্ষা করো।
5. Background mode manually enable → Android-এ foreground notification দেখা → স্ক্রিন বন্ধ করে “Hey Maya” → notification tap → mic। কাজ না করলে Stop করে আবার Enable দাও; ব্যাটারি optimiser ও Speech services যাচাই করো।

## উন্নয়নকারীদের জন্য

- `index.html` পুরোনো UI এবং অ্যাপের মূল JS। `setup-native.sh` Android bridge-এর Java class ও manifest edit করে।
- `.github/workflows/build-apk.yml` হলো APK build pipeline। `www` ফোল্ডার workflow-এ তৈরি হয়।
- পুরোনো অ্যাপের signing key এই আলাদা ZIP-এ নেই। ভবিষ্যতে Maya 2 আপডেট করতে একই release signing key ব্যবহার করা প্রয়োজন; debug-only app পুনরায় বিল্ড করলে key স্থায়ী নাও থাকতে পারে।
- `node --check` দিয়ে HTML থেকে JS script বের করে syntax পরীক্ষা এবং `bash -n setup-native.sh` চালানো যায়।
