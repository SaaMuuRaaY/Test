# 
# http://arquivoskodi.com.br

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMgICAgICBDb3B5cmlnaHQgKEMpIDIwMTkgZHJpbmZlcm5vbyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjDQojICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIw0KIyAgVGhpcyBQcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkgICAgICAgICMNCiMgIGl0IHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgYXMgcHVibGlzaGVkIGJ5ICAgICAgICAjDQojICB0aGUgRnJlZSBTb2Z0d2FyZSBGb3VuZGF0aW9uOyBlaXRoZXIgdmVyc2lvbiAyLCBvciAoYXQgeW91ciBvcHRpb24pICAgICAgICAgIw0KIyAgYW55IGxhdGVyIHZlcnNpb24uICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMNCiMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjDQojICBUaGlzIFByb2dyYW0gaXMgZGlzdHJpYnV0ZWQgaW4gdGhlIGhvcGUgdGhhdCBpdCB3aWxsIGJlIHVzZWZ1bCwgICAgICAgICAgICAgIw0KIyAgYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YgICAgICAgICAgICAgICMNCiMgIE1FUkNIQU5UQUJJTElUWSBvciBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRS4gU2VlIHRoZSAgICAgICAgICAgICAgICAjDQojICBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBmb3IgbW9yZSBkZXRhaWxzLiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIw0KIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMNCiMgIFlvdSBzaG91bGQgaGF2ZSByZWNlaXZlZCBhIGNvcHkgb2YgdGhlIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlICAgICAgICAgICAjDQojICBhbG9uZyB3aXRoIFhCTUM7IHNlZSB0aGUgZmlsZSBDT1BZSU5HLiAgSWYgbm90LCB3cml0ZSB0byAgICAgICAgICAgICAgICAgICAgIw0KIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbiwgNjc1IE1hc3MgQXZlLCBDYW1icmlkZ2UsIE1BIDAyMTM5LCBVU0EuICAgICAgICMNCiMgIGh0dHA6Ly93d3cuZ251Lm9yZy9jb3B5bGVmdC9ncGwuaHRtbCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQppbXBvcnQgeGJtYw0KaW1wb3J0IHhibWNndWkNCg0KaW1wb3J0IG9zDQppbXBvcnQgcmUNCg0KZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24uY29uZmlnIGltcG9ydCBDT05GSUcNCg0KDQpk'
love = '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'
god = 'ICAgICAgICAgICAgb3MucmVtb3ZlKGxpYikNCiAgICAgICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzLmRvd25sb2FkZXIgaW1wb3J0IERvd25sb2FkZXINCiAgICAgICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBleHRyYWN0DQogICAgICAgICAgICAgICAgRG93bmxvYWRlcigpLmRvd25sb2FkKHppcCwgbGliKQ0KICAgICAgICAgICAgICAgIHhibWMuc2xlZXAoMjAwMCkNCiAgICAgICAgICAgICAgICBwcm9ncmVzc19kaWFsb2cudXBkYXRlKDAsICdcbicrIkluc3RhbGFuZG8gezB9IGF0dWFsaXphw6fDo28iLmZvcm1hdChDT05GSUcuQURET05USVRMRSkpDQogICAgICAgICAgICAgICAgcGVyY2VudCwgZXJyb3JzLCBlcnJvciA9IGV4dHJhY3QuYWxsKGxpYiwgQ09ORklHLkFERE9OUywgVHJ1ZSkNCiAgICAgICAgICAgICAgICBwcm9ncmVzc19kaWFsb2cuY2xvc2UoKQ0KICAgICAgICAgICAgICAgIHhibWMuc2xlZXAoMTAwMCkNCiAgICAgICAgICAgICAgICBkYi5mb3JjZV9jaGVja191cGRhdGVzKGF1dG89VHJ1ZSwgb3Zlcj1UcnVlKQ0KICAgICAgICAgICAgICAgIHhibWMuc2xlZXAoMTAwMCkNCiAgICAgICAgICAgICAgICBsb2dnaW5nLmxvZ19ub3RpZnkoQ09ORklHLkFERE9OVElUTEUsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdbQ09MT1IgezB9XUFkZC1vbiB1cGRhdGVkWy9DT0xPUl0nLmZvcm1hdChDT05GSUcuQ09MT1IyKSkNCiAgICAgICAgICAgICAgICBsb2dnaW5nLmxvZygiW0F1dG8gVXBkYXRlIFdpemFyZF0gV2l6YXJkIHVwZGF0ZWQgdG8gdnswfSIuZm9ybWF0KHZlcikpDQogICAgICAgICAgICAgICAgdG9vbHMucmVtb3ZlX2ZpbGUob3MucGF0aC5qb2luKENPTkZJRy5BRERPTl9EQVRBLCAnc2V0dGluZ3MueG1sJykpDQogICAgICAgICAgICAgICAgd2luZG93LnNob3dfc2F2ZV9kYXRhX3NldHRpbmdzKCkNCiAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgbG9nZ2luZy5sb2coIltBdXRvIFVwZGF0ZSBXaXphcmRdIE5vdm8gV2l6YXJkIGRlIGluc3RhbGHDp8OjbyBpZ25vcmFkbzogezB9Ii5mb3JtYXQodmVyKSkNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIGxvZ2dpbmcubG9nKCJbQXV0byBVcGRhdGUgV2l6YXJkXSBTZW0gbm92YSB2ZXJzw6NvdnswfSIuZm9ybWF0KHZlcikpDQogICAgZWxzZToNCiAgICAgICAgbG9nZ2luZy5sb2coIltBdXRvIFVwZGF0ZSBXaXphcmRdIFVybCBwYXJhIG8gYXJxdWl2byBkbyBXaXphcmQgbsOjbyDDqSB2w6FsaWRvOiB7MH0iLmZvcm1hdChDT05GSUcuQlVJTERGSUxFKSkNCg0KDQpkZWYgYWRkb25fdXBkYXRlcyhkbz1Ob25lKToNCiAgICBzZXR0aW5nID0gJyJnZW5lcmFsLmFkZG9udXBkYXRlcyInDQogICAgaWYgZG8gPT0gJ3NldCc6DQogICAgICAgIHF1ZXJ5ID0gJ3t7Impzb25ycGMiOiIyLjAiLCAibWV0aG9kIjoiU2V0dGluZ3MuR2V0U2V0dGluZ1ZhbHVlIiwicGFyYW1zIjp7eyJzZXR0aW5nIjp7MH19fSwgImlkIjoxfX0nLmZvcm1hdChzZXR0aW5nKQ0KICAg'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))