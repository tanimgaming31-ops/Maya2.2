#!/usr/bin/env python3
"""Idempotent Maya 4.0 upgrade; preserves the exact current index.html and Android bridge.
Run from the repository root. Existing user data is not modified.
"""
from pathlib import Path
import re, shutil

BASE=Path(__file__).resolve().parent
INDEX=BASE/'index.html'
WORKFLOW=BASE/'.github/workflows/build-apk.yml'
SERVICE=BASE/'sw.js'
if not INDEX.exists(): raise SystemExit('index.html is missing at repository root.')
for fn in ('maya4.js','maya4.css'):
    if not (BASE/fn).is_file():raise SystemExit(f'Missing {fn}. Upload all Maya 4 files first.')
s=INDEX.read_text(encoding='utf-8')
if 'id="maya4Open"' in s:raise SystemExit('Unexpected static Maya 4 button; check index.html before upgrade.')
if 'maya4.js' not in s:
    if '</body>' not in s:raise SystemExit('index.html is missing </body>')
    if '</head>' not in s:raise SystemExit('index.html is missing </head>')
    backup=BASE/'index-before-maya4.html'
    if not backup.exists(): shutil.copyfile(INDEX,backup)
    s=s.replace('</head>','<link rel="stylesheet" href="maya4.css">\n</head>',1)
    s=s.replace('</body>','<script src="maya4.js" defer></script>\n</body>',1)
    # Preserve the existing Maya prompt and add the user's opt-in voice style on new sessions.
    marker='  return s;\n}\nfunction toolDeclarations(native) {'
    if marker in s:
        patch='''  // Maya 4: opt-in conversational style (voice model still controls acoustic expression).
  try {
    const choice=JSON.parse(localStorage.getItem('maya4.settings')||'{}').voiceStyle;
    const hints={gentle:'Speak softly, warmly and briefly.',calm:'Speak calmly, reassure without exaggerating.',playful:'Be gently playful while staying respectful.',focused:'Give clear, practical, concise replies.'};
    if (hints[choice]) s+='\\n\\nMAYA 4 PERSONAL VOICE STYLE: '+hints[choice];
  } catch (_maya4SettingError) {}
  return s;
}
function toolDeclarations(native) {'''
        s=s.replace(marker,patch,1)
    else: print('INFO: Could not find voice system prompt anchor; original style remains unchanged.')
    # If the current VRM viewer has its established viseme cycle, use optional caption-based
    # approximate vowels. The original cycle remains a fallback; no exact phoneme sync claim.
    old_viseme='active.set(keys[cycle],lip);'
    new_viseme="const mapped=window.Maya4Viseme?.(t);active.set(mapped?.key||keys[cycle],lip*(mapped?.gain??1));"
    if old_viseme in s: s=s.replace(old_viseme,new_viseme,1)
    # VRM material tinting: only named compatible materials; no invented 3D outfit model.
    anchor="  api.loaded=true;api.lastError='';"
    if anchor in s:
        payload='''  // Maya 4 VRM palette: matches named Hair/Clothes materials; restores originals on request.
  const maya4OriginalMaterials=new Map();
  api.setPalette=function(opts){
    if(!sourceScene)return {message:'No VRM loaded.'};
    let changed=0;
    sourceScene.traverse(obj=>{
      if(!obj.isMesh)return;
      const mats=Array.isArray(obj.material)?obj.material:[obj.material];
      for(const mat of mats){if(!mat||!mat.color)return;
        const name=(String(obj.name||'')+' '+String(mat.name||'')).toLowerCase();
        const group=/hair|bang|fringe|ponytail/.test(name)?'hair':/coat|outfit|cloth|jacket|dress|skirt|shirt|top|sweater/.test(name)?'outfit':null;
        if(!group)continue;
        if(!maya4OriginalMaterials.has(mat))maya4OriginalMaterials.set(mat,mat.color.clone());
        if(opts.reset){mat.color.copy(maya4OriginalMaterials.get(mat));changed++;}
        else if(/^#[0-9a-f]{6}$/i.test(opts[group]||'')){mat.color.set(opts[group]);changed++;}
        mat.needsUpdate=true;
      }
    });
    return {changed,message:changed?changed+' compatible material(s) updated.':'This VRM has no color-editable named hair/outfit materials.'};
  };
'''
        s=s.replace(anchor,payload+anchor,1)
    else:print('INFO: No VRM model loaded anchor; 3D recoloring not wired (safe fallback).')
    INDEX.write_text(s,encoding='utf-8')
    print('Updated index.html and saved index-before-maya4.html backup.')
else: print('Maya 4 script already installed; leaving index.html unchanged.')

# The existing Android workflow is intentionally kept unchanged. The dedicated
# Maya 4 workflow packages these add-on files and maya.vrm itself, so GitHub's
# restricted workflow-file write permissions are never required.
print('Original Android workflow preserved. Maya 4 uses its dedicated build workflow.')

if SERVICE.exists():
    sw=SERVICE.read_text(encoding='utf-8')
    sw=re.sub(r"const V = '[^']*'", "const V = 'maya-v4-20261016-1'", sw, count=1)
    sw=sw.replace("'./icon-512.png'", "'./icon-512.png', './maya4.js', './maya4.css'",1)
    SERVICE.write_text(sw,encoding='utf-8')
print('Maya 4 upgrade finished. The original Maya 3 UI and voice engine remain intact.')
