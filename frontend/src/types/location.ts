interface LocationPayload {
  id: number
  name: string
  file_upload: string
  in_folder: string
}

interface LocationItem {
  id: number
  name: string
  type: string
  file_upload: string
  children?: LocationItem[]
  in_folder?: string
}

class File implements LocationItem {
  id: number
  name: string
  type: string
  file_upload: string
  in_folder?: string

  constructor(id: number, name: string, type: string, fileUrl: string, inFolder?: string) {
    this.id = id
    this.name = name
    this.type = type
    this.file_upload = fileUrl
    this.in_folder = inFolder
  }
}

class Folder implements LocationItem {
  id: number
  name: string
  type: string
  file_upload: string
  children?: File[]

  constructor(id: number, name: string, fileUrl: string, children?: File[]) {
    this.id = id
    this.name = name
    this.file_upload = fileUrl
    this.children = children
    this.type = 'folder'
  }
}

export { File, Folder }
export type { LocationPayload, LocationItem }
