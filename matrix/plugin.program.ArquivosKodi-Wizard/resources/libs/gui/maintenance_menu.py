# 
# http://arquivoskodi.com.br

import base64, codecs
magic = 'IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0NCmltcG9ydCB4Ym1jDQoNCmltcG9ydCBvcw0KDQpmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgZGlyZWN0b3J5DQpmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgbG9nZ2luZw0KZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IHRvb2xzDQpmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbi5jb25maWcgaW1wb3J0IENPTkZJRw0KDQoNCmNsYXNzIE1haW50ZW5hbmNlTWVudToNCg0KICAgIGRlZiBnZXRfbGlzdGluZyhzZWxmKToNCiAgICAgICAgZGlyZWN0b3J5LmFkZF9kaXIoJ1tCXUxpbXBlemFbL0JdJywgeydtb2RlJzogJ21haW50JywgJ25hbWUnOiAnY2xlYW4nfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTEpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZGlyKCdbQl1BZGRvbiBUb29sc1svQl0nLCB7J21vZGUnOiAnbWFpbnQnLCAnbmFtZSc6ICdhZGRvbid9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMSkNCiAgICAgICAgZGlyZWN0b3J5LmFkZF9kaXIoJ1tCXU1hbnV0ZW7Dp8OjbyBkaXZlcnNhWy9CXScsIHsnbW9kZSc6ICdtYWludCcsICduYW1lJzogJ21pc2MnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTEpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZGlyKCdbQl1CYWNrVXAvUmVzdGF1cmFyWy9CXScsIHsnbW9kZSc6ICdtYWludCcsICduYW1lJzogJ2JhY2t1cCd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMSkNCiAgICAgICAgZGlyZWN0b3J5LmFkZF9kaXIoJ1tCXUFqdXN0ZXMvQ29ycmXDp8O1ZXMgZG8gc2lzdGVtYVsvQl0nLCB7J21vZGUnOiAnbWFpbnQnLCAnbmFtZSc6ICd0d2Vha3MnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTEpDQoNCiAgICBkZWYgY2xlYW5fbWVudShzZWxmKToNCiAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IHRvb2xzDQoNCiAgICAgICAgb24gPSAnW0JdW0NPTE9SIHNwcmluZ2dyZWVuXU9OWy9DT0xPUl1bL0JdJw0KICAgICAgICBvZmYgPSAnW0JdW0NPTE9SIHJlZF1PRkZbL0NPTE9SXVsvQl0nDQoNCiAgICAgICAgYXV0b2NsZWFuID0gJ3RydWUnIGlmIENPTkZJRy5BVVRPQ0xFQU5VUCA9PSAndHJ1ZScgZWxzZSAnZmFsc2UnDQogICAgICAgIGNhY2hlID0gJ3RydWUnIGlmIENPTkZJRy5BVVRPQ0FDSEUgPT0gJ3RydWUnIGVsc2UgJ2ZhbHNlJw0KICAgICAgICBwYWNrYWdlcyA9ICd0cnVlJyBpZiBDT05GSUcuQVVUT1BBQ0tBR0VTID09ICd0cnVlJyBlbHNlICdmYWxzZScNCiAgICAgICAgdGh1bWJzID0gJ3RydWUnIGlmIENPTkZJRy5BVVRPVEhVTUJTID09ICd0cnVlJyBlbHNlICdmYWxzZScNCiAgICAgICAgaW5jbHVkZXZpZCA9ICd0cnVlJyBpZiBDT05GSUcuSU5DTFVERVZJREVPID09ICd0cnVlJyBlbHNlICdmYWxzZScNCiAgICAgICAgaW5jbHVkZWFsbCA9ICd0cnVlJyBpZiBDT05GSUcuSU5DTFVERUFMTCA9PSAndHJ1ZScgZWxzZSAnZmFsc2UnDQoNCiAgICAgICAgc2l6ZXBhY2sgPSB0b29scy5nZXRfc2l6ZShDT05GSUcuUEFDS0FHRVMpDQogICAgICAgIHNpemV0aHVtYiA9IHRvb2xzLmdldF9zaXplKENPTkZJRy5USFVNQk5BSUxTKQ0KICAgICAgICBhcmNoaXZlID0gdG9vbHMuZ2V0X3NpemUoQ09ORklHLkFSQ0hJVkVfQ0FDSEUpDQogICAgICAgIHNpemVjYWNoZSA9IChjbGVhci5nZXRfY2FjaGVfc2l6ZSgpKSAtIGFyY2hpdmUNCiAgICAgICAgdG90YWxzaXplID0gc2l6ZXBhY2sgKyBzaXpldGh1bWIgKyBzaXplY2FjaGUNCg0KICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoDQogICAgICAgICAgICAnTGltcGV6YSBUb3RhbDogW0NPTE9SIHNwcmluZ2dyZWVuXVtCXXswfVsvQl1bL0NPTE9SXScuZm9ybWF0KHRvb2xzLmNvbnZlcnRfc2l6ZSh0b3RhbHNpemUpKSwgeydtb2RlJzogJ2Z1bGxjbGVhbid9LA0KICAgICAgICAgICAgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnTGltcGFyIENhY2hlOiBbQ09MT1Igc3ByaW5nZ3JlZW5dW0JdezB9Wy9CXVsvQ09MT1JdJy5mb3JtYXQodG9vbHMuY29udmVydF9zaXplKHNpemVjYWNoZSkpLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgeydtb2RlJzogJ2NsZWFyY2FjaGUnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihzY3JpcHQubW9kdWxlLnVybHJlc29sdmVyKScpIG9yIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoDQogICAgICAgICAgICAgICAgJ1N5c3RlbS5IYXNBZGRvbihzY3JpcHQubW9kdWxlLnJlc29sdmV1cmwpJyk6DQogICAgICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0xpbXBhciBjYWNoZXMgZGUgZnVuw6fDtWVzIGRlIHJlc29sdcOnw6NvJywgeydtb2RlJzogJ2NsZWFyZnVuY3Rpb25jYWNoZSd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0xpbXBhciBQYWNrYWdlczogW0NPTE9SIHNwcmluZ2dyZWVuXVtCXXswfVsvQl1bL0NPTE9SXScuZm9ybWF0KHRvb2xzLmNvbnZlcnRfc2l6ZShzaXplcGFjaykpLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgeydtb2RlJzogJ2NsZWFycGFja2FnZXMnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgNCiAgICAgICAgICAgICdMaW1wYXIgVGh1bWJuYWlsczogW0NPTE9SIHNwcmluZ2dyZWVuXVtCXXswfVsvQl1bL0NPTE9SXScuZm9ybWF0KHRvb2xzLmNvbnZlcnRfc2l6ZShzaXpldGh1bWIpKSwNCiAgICAgICAgICAgIHsnbW9kZSc6ICdjbGVhcnRodW1iJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICBpZiBvcy5wYXRoLmV4aXN0cyhDT05GSUcuQVJDSElWRV9DQUNIRSk6DQogICAgICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0xpbXBhciBBcmNoaXZlX0NhY2hlOiBbQ09MT1Igc3ByaW5nZ3JlZW5dW0JdezB9Wy9CXVsvQ09MT1JdJy5mb3JtYXQoDQogICAgICAgICAgICAgICAgdG9vbHMuY29udmVydF9zaXplKGFyY2hpdmUpKSwgeydtb2RlJzogJ2NsZWFyYXJjaGl2ZSd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKCdMaW1wYXIgdmVsaGFzIFRodW1ibmFpbHMnLCB7J21vZGUnOiAnb2xkVGh1bWJzJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0xpbXBhciBDcmFzaCBMb2dzJywgeydtb2RlJzogJ2NsZWFyY3Jhc2gnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnUHVyZ2UgRGF0YWJhc2VzJywgeydtb2RlJzogJ3B1cmdlZGInfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAg'
love = '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'
god = 'YWlhKScpOg0KICAgICAgICAgICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgNCiAgICAgICAgICAgICAgICAgICAgJy0tLSBJbmNsdWRlIEdhaWE6IHswfScuZm9ybWF0KGluY2x1ZGVnYWlhLnJlcGxhY2UoJ3RydWUnLCBvbikucmVwbGFjZSgnZmFsc2UnLCBvZmYpKSwNCiAgICAgICAgICAgICAgICAgICAgeydtb2RlJzogJ3RvZ2dsZWNhY2hlJywgJ25hbWUnOiAnaW5jbHVkZWdhaWEnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgICAgICBpZiB4Ym1jLmdldENvbmRWaXNpYmlsaXR5KCdTeXN0ZW0uSGFzQWRkb24ocGx1Z2luLnZpZGVvLm51bWJlcnNieW51bWJlcnMpJyk6DQogICAgICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKA0KICAgICAgICAgICAgICAgICAgICAnLS0tIEluY2x1ZGUgTnVNYjNyNTogezB9Jy5mb3JtYXQoaW5jbHVkZW51bWJlcnMucmVwbGFjZSgndHJ1ZScsIG9uKS5yZXBsYWNlKCdmYWxzZScsIG9mZikpLA0KICAgICAgICAgICAgICAgICAgICB7J21vZGUnOiAndG9nZ2xlY2FjaGUnLCAnbmFtZSc6ICdpbmNsdWRlbnVtYmVycyd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihwbHVnaW4udmlkZW8uc2NydWJzdjIpJyk6DQogICAgICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKA0KICAgICAgICAgICAgICAgICAgICAnLS0tIEluY2x1ZGUgU2NydWJzIHYyOiB7MH0nLmZvcm1hdChpbmNsdWRlc2NydWJzLnJlcGxhY2UoJ3RydWUnLCBvbikucmVwbGFjZSgnZmFsc2UnLCBvZmYpKSwNCiAgICAgICAgICAgICAgICAgICAgeydtb2RlJzogJ3RvZ2dsZWNhY2hlJywgJ25hbWUnOiAnaW5jbHVkZXNjcnVicyd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihwbHVnaW4udmlkZW8uc2VyZW4pJyk6DQogICAgICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKA0KICAgICAgICAgICAgICAgICAgICAnLS0tIEluY2x1ZGUgU2VyZW46IHswfScuZm9ybWF0KGluY2x1ZGVzZXJlbi5yZXBsYWNlKCd0cnVlJywgb24pLnJlcGxhY2UoJ2ZhbHNlJywgb2ZmKSksDQogICAgICAgICAgICAgICAgICAgIHsnbW9kZSc6ICd0b2dnbGVjYWNoZScsICduYW1lJzogJ2luY2x1ZGVzZXJlbid9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihwbHVnaW4udmlkZW8udGhlY3JldyknKToNCiAgICAgICAgICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoDQogICAgICAgICAgICAgICAgICAgICctLS0gSW5jbHVkZSBUSEUgQ1JFVzogezB9Jy5mb3JtYXQoaW5jbHVkZXRoZWNyZXcucmVwbGFjZSgndHJ1ZScsIG9uKS5yZXBsYWNlKCdmYWxzZScsIG9mZikpLA0KICAgICAgICAgICAgICAgICAgICB7J21vZGUnOiAndG9nZ2xlY2FjaGUnLCAnbmFtZSc6ICdpbmNsdWRldGhlY3Jldyd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihwbHVnaW4udmlkZW8udmVub20pJyk6DQogICAgICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKA0KICAgICAgICAgICAgICAgICAgICAnLS0tIEluY2x1ZGUgVmVub206IHswfScuZm9ybWF0KGluY2x1ZGV2ZW5vbS5yZXBsYWNlKCd0cnVlJywgb24pLnJlcGxhY2UoJ2ZhbHNlJywgb2ZmKSksDQogICAgICAgICAgICAgICAgICAgIHsnbW9kZSc6ICd0b2dnbGVjYWNoZScsICduYW1lJzogJ2luY2x1ZGV2ZW5vbSd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoJ1N5c3RlbS5IYXNBZGRvbihwbHVnaW4udmlkZW8ueW9kYSknKToNCiAgICAgICAgICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoDQogICAgICAgICAgICAgICAgICAgICctLS0gSW5jbHVkZSBZb2RhOiB7MH0nLmZvcm1hdChpbmNsdWRleW9kYS5yZXBsYWNlKCd0cnVlJywgb24pLnJlcGxhY2UoJ2ZhbHNlJywgb2ZmKSksDQogICAgICAgICAgICAgICAgICAgIHsnbW9kZSc6ICd0b2dnbGVjYWNoZScsICduYW1lJzogJ2luY2x1ZGV5b2RhJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKCctLS0gQXRpdmFyIHRvZG9zIFZpZGVvIEFkZG9ucycsIHsnbW9kZSc6ICd0b2dnbGVjYWNoZScsICduYW1lJzogJ3RydWUnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnLS0tIERlc2F0aXZhciB0b2RvcyBWaWRlbyBBZGRvbnMnLCB7J21vZGUnOiAndG9nZ2xlY2FjaGUnLCAnbmFtZSc6ICdmYWxzZSd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KDQogICAgZGVmIGFkZG9uX21lbnUoc2VsZik6DQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnUmVtb3ZlciBBZGRvbnMnLCB7J21vZGUnOiAncmVtb3ZlYWRkb25zJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICBkaXJlY3RvcnkuYWRkX2RpcignUmVtb3ZlciBBZGRvbiBEYXRhJywgeydtb2RlJzogJ3JlbW92ZWFkZG9uZGF0YSd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgZGlyZWN0b3J5LmFkZF9kaXIoJ0F0aXZhci9EZXNhdGl2YXIgQWRkb25zJywgeydtb2RlJzogJ2VuYWJsZWFkZG9ucyd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCiAgICAgICAgIyBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0VuYWJsZS9EaXNhYmxlIEFkdWx0IEFkZG9ucycsICd0b2dnbGVhZHVsdCcsIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQ0KICAgICAgICBkaXJlY3RvcnkuYWRkX2ZpbGUoJ0ZvcsOnYXIgYSBhdHVhbGl6YcOnw6NvIGRlIHRvZG9zIG9zIHJlcG9zaXTDs3Jpb3MnLCB7J21vZGUnOiAnZm9yY2V1cGRhdGUnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpDQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnRm9yw6dhciBhdHVhbGl6YcOnw6NvIGRlIHRvZG9zIG9zIGFkZG9ucycsIHsnbW9kZSc6ICdmb3JjZXVwZGF0ZScsICdhY3Rpb24nOiAnYXV0byd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykNCg0KICAgDQogICAgZGVmIGxvZ2dpbmdfbWVudShzZWxmKToNCiAgICAgICAgZXJyb3JzID0gaW50KGxvZ2dpbmcuZXJyb3JfY2hlY2tpbmcoY291bnQ9VHJ1ZSkpDQogICAgICAgIGVycm9yc2ZvdW5kID0gc3RyKGVycm9ycykgKyAnIEVycm9yKHMpIEZvdW5kJyBpZiBlcnJvcnMgPiAwIGVsc2UgJ05vbmUgRm91bmQnDQogICAgICAgIHdpemxvZ3NpemUgPSAnOiBbQ09MT1IgcmVkXU5vdCBGb3Vu'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))